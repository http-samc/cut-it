"""
    Main App
"""

import os
import sys
import webbrowser

import qtmodern.styles
import qtmodern.windows
import validators
from bs4 import BeautifulSoup
from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QShortcut

from GUI import GUI
from utils import data
from utils.bypass_browser import getBrowser
from utils.card import Card, Logger
from utils.citer import cite
from utils.clipboard_OSX import clipboard
from utils.distro import tagDisplay
from utils.export import printPDF
from utils.feedback import Feedback
from utils.ISD_theme import ISD
from utils.resource import PATH
from utils.text_scraper import text
from utils.updater import Updater
from utils.version_check import check, pollReleases

class main(GUI):
    """
        Adds logic to the GUI class
    """

    def __init__(self, isLight=False, ISD=False) -> None:
        super().__init__(isLight=isLight, ISD=ISD)

        # Close Event
        self.closeEvent = self._onClose

        # Defining ISD settings
        self.ISD = ISD

        # Error
        self.error = None

        # Setting Slots

            # Custom Emphasis Levels
        self.primary_em.clicked.connect(self._primaryEmphasis)
        self.secondary_em.clicked.connect(self._secondaryEmphasis)
        self.tertiary_em.clicked.connect(self._tertiaryEmphasis)

            # Generic Styling
        self.bold.clicked.connect(self._bold_)
        self.underline.clicked.connect(self._underline_)
        self.italics.clicked.connect(self._italic_)
        self.primary_highlight.clicked.connect(self._highlightP)
        self.secondary_highlight.clicked.connect(self._highlightS)
        self.minimize.clicked.connect(self._minimizeText)
        self.clearSelectionFormatting.clicked.connect(self._clearFormatting)

            # Misc
        self.autocut.clicked.connect(self._auto)
        self.autobypass.clicked.connect(self._autoBypass)
        self.shortcuts.currentTextChanged.connect(self._updateShortcut)
        self.shortcut_input.editingFinished.connect(self._saveShortcut)
        self.evidence_box.textChanged.connect(self._addDelimiter)
        self.cardSelector.currentIndexChanged.connect(self._cardSelectionChanged)
        self.tab_master.currentChanged.connect(self._tabChanged)
        self.theme.clicked.connect(self._toggleTheme)
        self.new_card.clicked.connect(self._newCard)
        self.open_card.clicked.connect(self._loadCard)
        self.delete_card.clicked.connect(self._deleteCard)
        self.copy_card.clicked.connect(self._copy)
        self.save_card.clicked.connect(self._print)
        self.updates.clicked.connect(self._updates)
        self.submit_feedback.clicked.connect(self._feedback)

        # Other __init__ reqs
        self._loadSettings(initialLoad = True)
        self._loadShortcuts()
        self.__loadAllCards()
        if not self.error: self._log()
        self._loadCard(initialLoad = True)
        self.hasClickedDeleteOnce = False

        # Prompt update if needed
        self._updater_()

        # Show docs if needed
        self._firstLoad_()

        # Refresh UI to prevent widget bugs
        self.showMinimized() 
        #self.showNormal()

    """
        Updater
    """
    def _updater_(self):
        """
            Determines whether to present an update window
        """

        data = pollReleases() # preventing excess GitHub API calls
        if not data: return

        # Create dialog and show it while forcing it to be resolved
        # prior to showing the main gui
        self.updateDialog = Updater(parent=self, data=data)
        self.updateDialog.exec_()

    """
        First Load
    """
    def _firstLoad_(self):
        "Opens Docs if needed"
        if not data.getFirstLoad(): return
        webbrowser.open("https://docs.cutit.cards", 1)
        data.setFirstLoad()

    """
        AutoBypass
    """
    def _autoBypass(self):
        """
            Generates Bypassed Browser
        """
        getBrowser()

    """
        Data Functions
    """
    def _loadSettings(self, initialLoad = False):
        """
            Loads all user data into instance vars
            Fills in UI with Settings if initialLoad
        """

        # Adding Preferences
        self._font_ = data.getPref("Font")
        self._zoom_ = data.getPref("Zoom")
        self.Primary_Highlight_Color = data.getPref("Primary Highlight Color")
        self.Secondary_Highlight_Color = data.getPref("Secondary Highlight Color")

        self.unscaled_Font_Size_Normal = data.getPref("Font Size of Normal Text")
        self.Font_Size_Normal = self.unscaled_Font_Size_Normal + self._zoom_

        font = QtGui.QFont()
        font.setFamily(self._font_)
        font.setPointSize(self.unscaled_Font_Size_Normal)
        self.evidence_box.setFont(font)

        self.unscaled_Font_Size_Min = data.getPref("Font Size of Minimized Text")
        self.Font_Size_Min = self._zoom_ + self.unscaled_Font_Size_Min

        self.Primary_Em = data.getPref("Primary Emphasis Settings")
        self.Secondary_Em = data.getPref("Secondary Emphasis Settings")
        self.Tertiary_Em = data.getPref("Tertiary Emphasis Settings")
        self.Font_Size_Primary_Em = self.Primary_Em[4] + self._zoom_
        self.Font_Size_Secondary_Em = self.Secondary_Em[4] + self._zoom_
        self.Font_Size_Tertiary_Em = self.Tertiary_Em[4] + self._zoom_
        self.Theme = data.getPref("Theme")

        # Adding Shortcuts
        self.primaryEmphasis = data.getShort("Primary Emphasis")
        self.secondaryEmphasis = data.getShort("Secondary Emphasis")
        self.tertiaryEmphasis = data.getShort("Tertiary Emphasis")
        self.clearFormatting = data.getShort("Clear Formatting")
        self.minimizeText = data.getShort("Minimize Text")
        self.newCard = data.getShort("Cut a New Card")
        self.autoPoll = data.getShort("AutoPoll")
        self.autoCite = data.getShort("AutoCite")
        self.autoCiteAndPoll = data.getShort("AutoPoll + AutoCite")
        self.print = data.getShort("Save As PDF")
        self.closeWindow = data.getShort("Close Window")

        # Set Zoom
        self.evidence_box.zoomIn(self._zoom_)
        if self.tertiaryEmphasis == "Ctrl+.": self.error = True

        self.__loadSettingsUI() if initialLoad else ... # We don't need to reapply settings to UI if user has already selected them

    def __loadSettingsUI(self):
        """
            Loads the Settings into the GUI
        """

        self.font.setCurrentText(self._font_)
        self.font_size_normal.setValue(self.unscaled_Font_Size_Normal)
        self.font_size_min.setValue(self.unscaled_Font_Size_Min)
        self.zoom.setValue(self._zoom_)
        self.highlight_1.setCurrentText(self.Primary_Highlight_Color)
        self.highlight_2.setCurrentText(self.Secondary_Highlight_Color)

        self.primary_bold.setCheckState(self.Primary_Em[0])
        self.primary_bold.setTristate(False)
        self.primary_italicised.setCheckState(self.Primary_Em[1])
        self.primary_italicised.setTristate(False)
        self.primary_underline.setCheckState(self.Primary_Em[2])
        self.primary_underline.setTristate(False)
        self.primary_highlight_2.setCurrentText(str(self.Primary_Em[3]))
        self.primary_size.setValue(self.Primary_Em[4])

        self.secondary_bold.setCheckState(self.Secondary_Em[0])
        self.secondary_bold.setTristate(False)
        self.secondary_italicised.setCheckState(self.Secondary_Em[1])
        self.secondary_italicised.setTristate(False)
        self.secondary_underline.setCheckState(self.Secondary_Em[2])
        self.secondary_underline.setTristate(False)
        self.secondary_highlight_2.setCurrentText(str(self.Secondary_Em[3]))
        self.secondary_size.setValue(self.Secondary_Em[4])

        self.tertiary_bold.setCheckState(self.Tertiary_Em[0])
        self.tertiary_bold.setTristate(False)
        self.tertiary_italicised.setCheckState(self.Tertiary_Em[1])
        self.tertiary_italicised.setTristate(False)
        self.tertiary_underline.setCheckState(self.Tertiary_Em[2])
        self.tertiary_underline.setTristate(False)
        self.tertiary_highlight.setCurrentText(str(self.Tertiary_Em[3]))
        self.tertiary_size.setValue(self.Tertiary_Em[4])

        all_shortcuts = data.getPrefData()["shortcuts"]
        for shortcut in list(all_shortcuts.keys()):
            self.shortcuts.addItem(shortcut)

    def _updateShortcut(self):
        """
            Updates shortcut when user wants to view a separate one
        """

        try:
            newSequence = data.getShort(self.shortcuts.currentText())
        except KeyError:
            return
        if newSequence == 'Choose a shortcut to view/edit . . . (applies on restart)':
            return
        self.shortcut_input.setKeySequence(newSequence)

    def _saveShortcut(self):
        """
            Saves shortcut to memory when user is done editing
        """

        currentSequence = self.shortcut_input.keySequence()
        data.setShort(self.shortcuts.currentText(), currentSequence.toString())

    def _loadShortcuts(self):
        """
            Inits custom keybindings for all user-defined shortcuts
        """

        self.clearFormatting_ = QShortcut(QtGui.QKeySequence(self.clearFormatting), self.evidence_box) # Standard alternative
        self.clearFormatting_.activated.connect(self._clearFormatting)

        self.primaryEmphasis_ = QShortcut(QtGui.QKeySequence(self.primaryEmphasis), self.evidence_box)
        self.primaryEmphasis_.activated.connect(self._primaryEmphasis)

        self.secondaryEmphasis_ = QShortcut(QtGui.QKeySequence(self.secondaryEmphasis), self.evidence_box)
        self.secondaryEmphasis_.activated.connect(self._secondaryEmphasis)

        self.tertiaryEmphasis_ = QShortcut(QtGui.QKeySequence(self.tertiaryEmphasis), self.evidence_box)
        self.tertiaryEmphasis_.activated.connect(self._tertiaryEmphasis)

        self.minimizeText_ = QShortcut(QtGui.QKeySequence(self.minimizeText), self.evidence_box)
        self.minimizeText_.activated.connect(self._minimizeText)

        self.newCard_ = QShortcut(QtGui.QKeySequence(self.newCard), self.evidence_box)
        self.newCard_.activated.connect(self._newCard)

        self.autoPoll_ = QShortcut(QtGui.QKeySequence(self.autoPoll), self.evidence_box)
        self.autoPoll_.activated.connect(self._autoPoll)

        self.autoCite_ = QShortcut(QtGui.QKeySequence(self.autoCite), self.evidence_box)
        self.autoCite_.activated.connect(self._autoCite)

        self.autoCiteAndPoll_ = QShortcut(QtGui.QKeySequence(self.autoCiteAndPoll), self.evidence_box)
        self.autoCiteAndPoll_.activated.connect(self._autoCiteAndPoll)

        self.print_ = QShortcut(QtGui.QKeySequence(self.print), self.evidence_box)
        self.print_.activated.connect(self._print)

        self.closeWindow_ = QShortcut(QtGui.QKeySequence(self.closeWindow), self.evidence_box)
        self.closeWindow_.activated.connect(self._onClose)

        self.closeWindow__ = QShortcut(QtGui.QKeySequence(self.closeWindow), self.feedback)
        self.closeWindow__.activated.connect(self._onClose)

        self.closeWindow___ = QShortcut(QtGui.QKeySequence(self.closeWindow), self.distro)
        self.closeWindow___.activated.connect(self._onClose)

    def _saveSettings(self):
        """
            Saves settings to data.json
        """

        data.setPref("Font", self.font.currentText())
        # Allow zoom reapplication w/o reboot
        data.setPref("Zoom", self.zoom.value())
        data.setPref("Primary Highlight Color", self.highlight_1.currentText())
        data.setPref("Secondary Highlight Color", self.highlight_2.currentText())
        data.setPref("Font Size of Normal Text", self.font_size_normal.value())
        data.setPref("Font Size of Minimized Text", self.font_size_min.value())
        data.setPref("Primary Emphasis Settings", [
            self.primary_bold.isChecked(),
            self.primary_italicised.isChecked(),
            self.primary_underline.isChecked(),
            self.primary_highlight_2.currentText(),
            self.primary_size.value()
        ])
        data.setPref("Secondary Emphasis Settings", [
            self.secondary_bold.isChecked(),
            self.secondary_italicised.isChecked(),
            self.secondary_underline.isChecked(),
            self.secondary_highlight_2.currentText(),
            self.secondary_size.value()
        ])
        data.setPref("Tertiary Emphasis Settings", [
            self.tertiary_bold.isChecked(),
            self.tertiary_italicised.isChecked(),
            self.tertiary_underline.isChecked(),
            self.tertiary_highlight.currentText(),
            self.tertiary_size.value()
        ])

    """
        Misc. Utils
    """
    def _updates(self):
        """
            Changes text of button to notify if update is needed or not
        """

        self.updates.setText(check())

    def _feedback(self):
        """
            Submits feedback
        """

        self.t2 = Feedback(message=self.feedback.toPlainText())
        self.t2.start()
        self.feedback.clear()

    def _toggleTheme(self):
        """
            Changes theme from current to reciprocal (applies on reboot)
            (eg. light -> dark, dark -> light)
        """

        # Define current theme, new theme
        currentTheme = data.getPref("Theme")
        newTheme = "light" if currentTheme == "dark" else "dark"
        self.isLight = True if newTheme == "light" else False
        GUI.updateStyling(self)

        # Change theme on current instance
        if newTheme == "light" and not self.ISD: qtmodern.styles.light(app)
        elif newTheme == "light" and self.ISD: ISD(app)
        else: qtmodern.styles.dark(app)

        # Store new preference for future instances
        data.setPref("Theme", newTheme)

    def _addDelimiter(self):
        """
            Triggered when the evidence box's text changes
            Adds closing bracket ] when an opening one [ is typed
        """

        cursor = self.evidence_box.textCursor()
        if cursor.hasSelection():
            return None

        START = cursor.selectionStart()-1
        if START < 0:
            return None

        cursor.setPosition(START, QtGui.QTextCursor.KeepAnchor)
        latestChar = cursor.selectedText()

        if latestChar == "[":
            cursor.clearSelection()
            cursor.setPosition(START+1, QtGui.QTextCursor.KeepAnchor)
            cursor.insertText("[] ")
            cursor.setPosition(START+1, QtGui.QTextCursor.MoveAnchor)
            self.evidence_box.setTextCursor(cursor)

    def _toHTML(self, copy = False, isForExport = False):
        """
            Returns list: [text of card, html of card]
            Copies plain & rich text to clipboard IFF :param: copy -> True
        """

        doc = self.evidence_box.document()
        soup = BeautifulSoup(doc.toHtml(), 'html.parser')
        paragraphs = soup.find_all('p')
        html = ""

        for p in paragraphs:
            html += str(p)

        html = html.replace('<br>', ' ')

        # Formatting for export
        if copy or isForExport:
            html = html.replace('font-weight:600;', 'font-weight:bold;')
            html = html.replace(f'font-size:{self.Font_Size_Min}pt;', f'font-size:{self.unscaled_Font_Size_Min}pt;')
            html = html.replace(f'font-size:{self.Font_Size_Normal}pt;', f'font-size:{self.unscaled_Font_Size_Normal}pt;')
            html = html.replace(f'font-size:{self.Font_Size_Primary_Em}pt;', f'font-size:{self.Primary_Em[4]}pt;')
            html = html.replace(f'font-size:{self.Font_Size_Secondary_Em}pt;', f'font-size:{self.Secondary_Em[4]}pt;')
            html = html.replace(f'font-size:{self.Font_Size_Tertiary_Em}pt;', f'font-size:{self.Tertiary_Em[4]}pt;')

        html = f'<body style="font-size: {self.Font_Size_Normal}pt; font-family: {self._font_}">' + html + '</body>'

        text = str(soup.text)[2:]

        clipboard.add(text, html) if copy else ...

        return [text, html]

    def _auto(self, autoCite = False, autoPoll = False):
        """
            Adds MLA & Debate-Grade Citation and/or article text to evidence box
        """

        html = f"<p>"
        URL = self.link.text()

        if not validators.url(URL):
            return

        # Adding Citation if appropriate
        if self.autocite.isChecked() or autoCite:

            self.autocite.setCheckState(False)

            CREDS = self.creds.text()
            TAG = self.warrant.text()

            try:
                self.msg.clear()
                self.msg.setText("Getting citation . . .")
                citation = cite(URL)
                missingAttrs = citation.getMissingAttrs()
                if missingAttrs:
                    msgStr = "We weren't able to find the following information from the URL - you'll have to enter it manually: "
                    for attr in missingAttrs:
                        msgStr += attr + ", "
                    self.msg.clear()
                    self.msg.setText(msgStr[:-2])

            except Exception:
                self.msg.clear()
                self.msg.setText("Sorry, there was an error getting your citation.")
                return

            debate_citation = citation.debate()
            mla_citation = citation.mla()

            if TAG != "":
                html += f"""
                <span style='background-color: yellow; font-size: {self.Font_Size_Primary_Em}pt;'><u><strong>
                    {TAG}
                </strong></u></span><br>
                """

            html += f"""
            <span style='background-color: cyan; font-size: {self.Font_Size_Primary_Em}pt;'><u><strong>
                {debate_citation[0]} '{debate_citation[1]}<br>
            </strong></u></span>
            """

            if CREDS != "":
                html += f"""
                <i>
                {CREDS}<br>
                </i>
                """

            html += f"""
                {debate_citation[2]} • {debate_citation[3]}<br>
                {mla_citation}<br><br>
            """

        # Adding Article Text if appropriate
        if self.autopoll.isChecked() or autoPoll:

            self.autopoll.setCheckState(False)

            try:
                self.msg.clear()
                self.msg.setText("Polling text . . .")
                article = text.scrape(URL)
                html += article

            except Exception:
                self.msg.clear()
                self.msg.setText(f"Sorry, we can't support {URL}! Please use our Chrome Extension instead.")

            html += "</p>"

        # Inserting Text
        cursor = self.evidence_box.textCursor()
        cursor.setPosition(0)
        cursor.insertHtml(html)

        self._toHTML(copy = True)
        self.msg.clear()
        self.msg.setText("AutoCut complete!")

    def _copy(self):
        """
            Copies card to clipboard
        """

        self._toHTML(copy = True)

    def _onClose(self, event = None):
        """
            Behavior for window close (saves card first)
        """

        self._newCard()

        if len(self.cardSelector.currentText()) >= 1:
            self.index = self.cardSelector.currentText()[:self.cardSelector.currentText().find(":")]

            try:
                self.index = int(self.index)

            except Exception:
                self.index = None
        else:
            self.index = None

        data.setIndex(self.index)
        self._saveSettings()

        event.accept() if event else self.close()

    def _tabChanged(self):
        """
            Saves settings and reapplies them on tab change
        """

        self._saveSettings()
        self._loadSettings()

    def _log(self):
        """
            Posts objs to API for efficacy monitoring & GitHub badge stats
        """

        self.t1 = Logger(cards = data.getCardData()["cards"])
        self.t1.start()

    """
        Card History Utilities
    """
    def __loadAllCards(self):
        """
            Adds all cards to card history selector
        """

        # Clearing all data in combobox
        self.cardSelector.clear()
        self.cardSelector.addItem("Select Card & open with 'Open Selection'")

        cards = data.getCardData()["cards"]

        # Running Index counter
        self.cardIndex = 0 # current max index of card selector

        for card in cards:

            card = Card(**card) # Construct Card from dict

            # If we have a tagline, use that as a primary identifier
            TAG = card.TAG.replace('\t', '').replace('\n', '')
            TEXT = card.TEXT.replace('\t', '').replace('\n', '')

            if TAG.replace(' ', '') != "":
                self.cardSelector.addItem(f"{self.cardIndex}: {TAG} - {TEXT}")

            # Or just use the card text
            else:
                self.cardSelector.addItem(f"{self.cardIndex}: {TEXT}")

            # Move to next index (we won't have blanks due to the filtering in _saveCard w/ Card.isCard())
            self.cardIndex += 1

    def _saveCard(self) -> bool:
        """
            Saves current card if it has data (is not blank)
        """

        evidence_data = self._toHTML()

        # Create Card
        card = Card(
            self.warrant.text(),
            self.creds.text(),
            self.link.text(),
            evidence_data[0],
            evidence_data[1]
        )

        # Return if card has no data (avoid saving blank cards to .json)
        if not card.isCard():
            return False

        if self.index is None:
            data.addCard(card)

        else:
            data.addCard(card, idx = self.index)

        return True

    def _newCard(self):
        """
            Saves old card and opens new one
        """

        # Save card
        self._saveCard()

        # Prepare new card framework
        self._addToCardSelector()
        self.autocite.setCheckState(True)
        self.autocite.setTristate(False)
        self.autopoll.setCheckState(True)
        self.autopoll.setTristate(False)
        document = self.evidence_box.document()
        document.clear()
        self.warrant.setText("")
        self.creds.setText("")
        self.link.setText("")
        self.index = None
        self.cardSelector.setCurrentIndex(0)

    def _loadCard(self, initialLoad = False):
        """
            Loads most recent card (saves previous one as well and adds to card selector)
        """

        if len(self.cardSelector.currentText()) >= 1 and not self.cardSelector.currentText()[0].isnumeric():
            self.index = None
            return

        # Add to selector, recheck auto's
        if not initialLoad:
            self._addToCardSelector()
            self.autocite.setCheckState(True)
            self.autocite.setTristate(False)
            self.autopoll.setCheckState(True)
            self.autopoll.setTristate(False)
            self._saveCard()

        # Get index of most recent card
        if len(self.cardSelector.currentText()) >= 1:
            self.index = data.getIndex() if initialLoad else self.cardSelector.currentText()[:self.cardSelector.currentText().find(":")]

        else:
            self.index = None

        # Convert to int if appropriate
        try:
            self.index = int(self.index)

        except Exception:
            self.index = None

        # Clear Fields
        document = self.evidence_box.document()
        document.clear()

        if self.index is None:
            self.warrant.setText("")
            self.creds.setText("")
            self.link.setText("")
            return

        # If we do have a card, get it and set all the respective attrs in the GUI
        card = data.getCard(self.index)

        # If we don't have a previous card -> Set all fields as empty and return
        if self.index is None or card is None:
            self.warrant.setText("")
            self.creds.setText("")
            self.link.setText("")
            return

        self.warrant.setText(card.TAG)
        self.creds.setText(card.CREDS)
        self.link.setText(card.URL)
        self.cardSelector.setCurrentIndex(self.index + 1)

        # Insert html
        cursor = self.evidence_box.textCursor()
        cursor.insertHtml(card.HTML)
        cursor.setPosition(0, QtGui.QTextCursor.MoveAnchor)
        self.evidence_box.setTextCursor(cursor)

    def _deleteCard(self):
        """
            Deletes currently open card after second click for safety
        """

        if self.hasClickedDeleteOnce:

            data.deleteCard(self.index)

            # Clearing fields
            self.msg.clear()
            self.warrant.setText("")
            self.creds.setText("")
            self.link.setText("")
            document = self.evidence_box.document()
            document.clear()

            # Removing from card selector
            try:
                if len(self.cardSelector.currentText()) > 0:
                    currentIndex = int(self.cardSelector.currentText()[:self.cardSelector.currentText().find(":")])
                else:
                    currentIndex = None

            except Exception:
                currentIndex = None

            self.cardSelector.removeItem(currentIndex + 1) if currentIndex is not None else self.cardSelector.setCurrentIndex(0)

            self.msg.setText("Card deleted successfully!")
            self.hasClickedDeleteOnce = False

            # Reload all cards to avoid index errors
            self.__loadAllCards()

        else:

            # If the card in Card Selector isn't what is actually open, alert user.
            try:
                if len(self.cardSelector.currentText()) > 0:
                    currentIndex = int(self.cardSelector.currentText()[:self.cardSelector.currentText().find(":")])

                else:
                    currentIndex = None

            except Exception:
                currentIndex = None

            if (currentIndex is not None) and (currentIndex != self.index):
                self.msg.clear()
                message = "<b>WARNING!</b> You are attempting to delete the card that is currently open, "
                message += "NOT what is selected in the Card History bar. If you want to proceed, click the delete button again."
                self.msg.insertHtml(message)

            else:
                self.msg.clear()
                self.msg.setText("""You are attempting to delete the currently opened card. Click the delete button again to confirm.""")

            self.hasClickedDeleteOnce = True

    def _addToCardSelector(self):
        """
            Adds current card to card selector
        """

        # If the card already has an index, it already exists in the selector
        if self.index is not None:
            return

        # Create Card
        evidence_data = self._toHTML()

        card = Card(
            self.warrant.text(),
            self.creds.text(),
            self.link.text(),
            evidence_data[0],
            evidence_data[1]
        )

        # If the card isn't a card, don't add it
        if not card.isCard():
            return

        # Add card to selector
        TAG = card.TAG.replace('\t', '').replace('\n', '')
        TEXT = card.TEXT.replace('\t', '').replace('\n', '')

        if TAG.replace(' ', '') != "":
            self.cardSelector.addItem(f"{self.cardIndex}: {TAG} - {TEXT}")
        else:
            self.cardSelector.addItem(f"{self.cardIndex}: {TEXT}")

        self.cardIndex += 1

    def _cardSelectionChanged(self):
        """
            Resets the delete status (clicked once) if the selected card changes
        """

        self.hasClickedDeleteOnce = False

    """
        Shortcut Functions
    """
    def _autoCiteAndPoll(self):
        """
            Adds MLA & Debate-Grade Citation & article text to evidence box
        """

        self._auto(True, True)

    def _autoCite(self):
        """
            Adds MLA & Debate-Grade Citation to evidence box
        """

        self._auto(True, False)

    def _autoPoll(self):
        """
            Adds article text to evidence box
        """

        self._auto(False, True)

    def _print(self):
        """
            Triggers User Input for Directory and Saves Card as PDF
        """

        self.msg.clear()
        self.msg.setText("Printing card . . .")

        # Getting Current User's Home Dir
        startingDir = os.path.expanduser("~")

        # Getting input for target dir
        destDir = QFileDialog.getExistingDirectory(None,
                'Folder To Save In',
                startingDir,
                QFileDialog.ShowDirsOnly)

        # Getting HTML, filename
        html = self._toHTML(isForExport = True)[1]
        cardName = self.warrant.text() if self.warrant.text() != "" else "Cut-It Export"

        path = f"{destDir}"

        try:
            if path == "":
                self.msg.clear()
                self.msg.setText("Invalid destination selected.")
                return

            printPDF(html, path, cardName = cardName)
            self.msg.clear()
            self.msg.setText("Saved PDF Successfully!")

        except Exception as e:
            self.msg.clear()
            self.msg.setText("There was an error saving your .pdf.")

    """
        High-Level Emphasis Functions
    """
    def __getSelectedText(self) -> tuple:
        """
            Returns cursor's start index and currently selected text in a tuple
        """

        # Get text cursor
        cursor = self.evidence_box.textCursor()

        # If there's no selection return None
        if not cursor.hasSelection():
            return None

        # Return tuple
        return (cursor.selectionStart(), cursor.selectedText())

    def __addText(self, html, index):
        """
            Inserts formatted text at cursor position and reselects text
            Copies text to clipboard
        """

        # Get text cursor
        cursor = self.evidence_box.textCursor()

        # Add HTML
        cursor.insertHtml(html)

        # Reset Position
        cursor.setPosition(index, QtGui.QTextCursor.KeepAnchor)

        # Copy to clipboard
        self._toHTML(copy=True)

    """
        Mid-Level Emphasis Functions
    """
    def _primaryEmphasis(self):
        """
            Styles text with Primary Emphasis
        """

        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        text = selection_data[1]

        text = self._bold(text) if self.Primary_Em[0] else text
        text = self._italic(text) if self.Primary_Em[1] else text
        text = self._underline(text) if self.Primary_Em[2] else text
        text = self._highlight(text, self.Primary_Em[3]) if self.Primary_Em[3] != None else text
        text = f'<span style="font-size:{self.Font_Size_Primary_Em}pt">{text}</span>'

        self.__addText(text, selection_data[0])
        self._toHTML(copy = True)

    def _secondaryEmphasis(self):
        """
            Styles text with Secondary Emphasis
        """

        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        text = selection_data[1]

        text = self._bold(text) if self.Secondary_Em[0] else text
        text = self._italic(text) if self.Secondary_Em[1] else text
        text = self._underline(text) if self.Secondary_Em[2] else text
        text = self._highlight(text, self.Secondary_Em[3]) if self.Secondary_Em[3] != None else text
        text = f'<span style="font-size:{self.Font_Size_Secondary_Em}">{text}</span>'

        self.__addText(text, selection_data[0])
        self._toHTML(copy = True)

    def _tertiaryEmphasis(self):
        """
            Styles text with Tertiary Emphasis
        """

        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        text = selection_data[1]

        text = self._bold(text) if self.Tertiary_Em[0] else text
        text = self._italic(text) if self.Tertiary_Em[1] else text
        text = self._underline(text) if self.Tertiary_Em[2] else text
        text = self._highlight(text, self.Tertiary_Em[3]) if self.Tertiary_Em[3] != None else text
        text = f'<span style="font-size:{self.Font_Size_Tertiary_Em}">{text}</span>'

        self.__addText(text, selection_data[0])
        self._toHTML(copy = True)

    def _highlightP(self):
        """
            Highlights text with Primary Highlight Color
        """

        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        HTML = f"<span style='background-color: {self.Primary_Highlight_Color}'>{selection_data[1]}</span>"
        self.__addText(HTML, selection_data[0])
        self._toHTML(copy = True)

    def _highlightS(self):
        """
            Highlights text with Secondary Highlight Color
        """

        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        HTML = f"<span style='background-color: {self.Secondary_Highlight_Color}'>{selection_data[1]}</span>"
        self.__addText(HTML, selection_data[0])
        self._toHTML(copy = True)

    def _bold_(self):
        """
            Bolds selected text
        """

        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        self.__addText(self._bold(selection_data[1]), selection_data[0])
        self._toHTML(copy = True)

    def _underline_(self):
        """
            Underlines selected text
        """

        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        self.__addText(self._underline(selection_data[1]), selection_data[0])
        self._toHTML(copy = True)

    def _italic_(self):
        """
            Italicises selected text
        """

        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        self.__addText(self._italic(selection_data[1]), selection_data[0])
        self._toHTML(copy = True)

    def _clearFormatting(self):
        """
            Clears Formatting on selected text
        """

        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        cursor = self.evidence_box.textCursor()
        cursor.insertHtml(f"<span>{selection_data[1]}</span>")
        self._toHTML(copy = True)

    def _minimizeText(self):
        """
            Minimizes Text
        """

        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        HTML = f'<span style="font-size: {self.Font_Size_Min}pt;">{selection_data[1]}</span>'
        self.__addText(HTML, selection_data[0])
        self._toHTML(copy = True)

    """
        Low-Level Emphasis Functions
    """
    def _bold(self, text):
        """
            Returns bolded version of :param: text
        """

        return f"<b>{text}</b>"

    def _underline(self, text):
        """
            Returns underlined version of :param: text
        """

        return f"<u>{text}</u>"

    def _italic(self, text):
        """
            Returns italicised version of :param: text
        """

        return f"<em>{text}</em>"

    def _highlight(self, text, color):
        """
            Returns highlighted version of :param: text of the color :param: color
        """

        return f"<span style='background-color: {color}'>{text}</span>"

if __name__ == "__main__":
    # Initialize User Data
    data.init()

    # Create App
    global app
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_Use96Dpi)
    app = QtWidgets.QApplication(sys.argv)

    font = QtGui.QFont()
    font.setPointSize(12)
    app.setFont(font)

    # Handling themes
    if data.getPref("Theme") == "light" and "ISD" in tagDisplay():
        ISD(app)
        isLight = True
        isISD = True

    elif data.getPref("Theme") == "light":
        qtmodern.styles.light(app)
        isLight = True
        isISD = False

    else:
        qtmodern.styles.dark(app)
        isLight = False
        isISD = False

    gui = main(isLight=isLight, ISD=isISD)
    #gui = qtmodern.windows.ModernWindow(gui)
    gui.show()
    sys.exit(app.exec_())