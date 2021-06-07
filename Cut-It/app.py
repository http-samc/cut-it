from PyQt5.QtWidgets import (QFileDialog, QMainWindow, QPlainTextEdit, QApplication, QShortcut, QWidget)
from PyQt5 import QtCore, QtGui, QtWidgets
from utils.clipboard_WIN import clipboard # TODO Consolidate to 1 clipboard class
from utils.text_scraper import text
from bs4 import BeautifulSoup
from utils.citer import cite
from utils.card import Card
import qtmodern.windows
from utils import data
import qtmodern.styles
from PyQt5 import Qt
from GUI import GUI
import validators
import sys
import os

# TODO add init data protocols for cards and prefs

class main(GUI):
    """
        Adds logic to the GUI class
    """

    def __init__(self, isLight=False) -> None:
        super().__init__(isLight=isLight)

        # Close Event
        self.closeEvent = self._onClose

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

            # Misc
        self.copy.clicked.connect(self._copy)
        self.autocut.clicked.connect(self._autoCiteAndPoll)

        # Signals
        self.evidence_box.textChanged.connect(self._addDelimiter)
        self.cardSelector.currentIndexChanged.connect(self._cardSelectionChanged)

        # Other _init_ reqs
        self._loadSettings()
        self._loadShortcuts()
        self._loadCard()
        self.hasClickedDeleteOnce = False
    
    """
        Data Functions
    """
    def _loadSettings(self):
        """
            Loads all user data into instance vars
        """

        # Adding Preferences
        self.font = data.getPref("Font")
        self.Primary_Highlight_Color = data.getPref("Primary Highlight Color")
        self.Secondary_Highlight_Color = data.getPref("Secondary Highlight Color")
        self.Font_Size_Primary_Em = data.getPref("Font Size of Primary Emphasis")
        self.Font_Size_Secondary_Em = data.getPref("Font Size of Secondary Emphasis")
        self.Font_Size_Tertiary_Em = data.getPref("Font Size of Tertiary Emphasis")
        self.Font_Size_Normal = data.getPref("Font Size of Normal Text")
        self.Font_Size_Min = data.getPref("Font Size of Minimized Text")
        self.Primary_Em = data.getPref("Primary Emphasis Settings")
        self.Secondary_Em = data.getPref("Secondary Emphasis Settings")
        self.Tertiary_Em = data.getPref("Tertiary Emphasis Settings")
        self.Theme = data.getPref("Theme")

        # Adding Shortcuts
        self.primaryEmphasis = data.getShort("Primary Emphasis")
        self.secondaryEmphasis = data.getShort("Secondary Emphasis")
        self.tertiaryEmphasis = data.getShort("Tertiary Emphasis")
        self.minimizeText = data.getShort("Minimize Text")
        self.autoPoll = data.getShort("AutoPoll")
        self.autoCite = data.getShort("AutoCite")
        self.autoCiteAndPoll = data.getShort("AutoPoll + AutoCite")
        self.print = data.getShort("Save As PDF")
        self.closeWindow = data.getShort("Close Window")

    def _loadShortcuts(self):
        """
            Inits custom keybindings for all user-defined shortcuts
        """
        
        # TODO Keep Selected Text, Find (ctrl+f)

        clearFormatting = QShortcut(QtGui.QKeySequence('Ctrl+Z'), self.evidence_box)
        clearFormatting.activated.connect(self._clearFormatting)

        primaryEmphasis = QShortcut(QtGui.QKeySequence(self.primaryEmphasis), self.evidence_box)
        primaryEmphasis.activated.connect(self._primaryEmphasis)

        secondaryEmphasis = QShortcut(QtGui.QKeySequence(self.secondaryEmphasis), self.evidence_box)
        secondaryEmphasis.activated.connect(self._secondaryEmphasis)

        tertiaryEmphasis = QShortcut(QtGui.QKeySequence(self.tertiaryEmphasis), self.evidence_box)
        tertiaryEmphasis.activated.connect(self._tertiaryEmphasis)

        minimizeText = QShortcut(QtGui.QKeySequence(self.minimizeText), self.evidence_box)
        minimizeText.activated.connect(self._minimizeText)

        autoPoll = QShortcut(QtGui.QKeySequence(self.autoPoll), self.evidence_box)
        autoPoll.activated.connect(self._autoPoll)

        autoCite = QShortcut(QtGui.QKeySequence(self.autoCite), self.evidence_box)
        autoCite.activated.connect(self._autoCite)

        autoCiteAndPoll = QShortcut(QtGui.QKeySequence(self.autoCiteAndPoll), self.evidence_box)
        autoCiteAndPoll.activated.connect(self._autoCiteAndPoll)

        print = QShortcut(QtGui.QKeySequence(self.print), self.evidence_box)
        print.activated.connect(self._print)

        closeWindow = QShortcut(QtGui.QKeySequence(self.closeWindow), self.evidence_box)
        closeWindow.activated.connect(self._closeWindow)

    """
        Misc. Utils
    """
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

    def _toHTML(self, copy = False):
        """
            Returns list: [text of card, html of card]
            Copies plain & rich text to clipboard IFF :param: copy -> True
        """

        doc = self.evidence_box.document()
        soup = BeautifulSoup(doc.toHtml(), 'html.parser')
        html = str(soup.find('p'))
        html = html.replace('600', 'bold')
        html = f'<body style="font-family: {self.font}">' + html + '</body>'
        text = str(soup.text)

        clipboard.add(text, html) if copy else ...
        return [text, html]

    def _auto(self, autoCite, autoPoll):
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
                citation = cite(URL)
                # TODO check for missing information by notifying user
            
            except Exception:
                self.msg.setPlainText("Sorry, there was an error getting your citation.")
                return

            debate_citation = citation.debate()
            mla_citation = citation.mla() 

            if TAG != "":
                html += """
                <span style='background-color: yellow; font-size: 12pt;'><u><strong>
                    {TAG}
                </strong></u></span><br>
                """
            
            html += f"""
            <span style='background-color: cyan; font-size: 12pt;'><u><strong>
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
                article = text.scrape(URL)
                html += article

            except Exception:
                self.msg.setPlainText(f"Sorry, we can't support {URL}! Please use our Chrome Extension instead.")

            html += "</p>"
        
        # Inserting Text
        cursor = self.evidence_box.textCursor()
        cursor.setPosition(0)
        cursor.insertHtml(html)

    def _copy(self):
        """
            Copies card to clipboard
        """

        self._toHTML(copy = True)

    def _onClose(self, event):
        """
            Behavior for window close (saves card first)
        """

        self._saveCard()
        event.accept()
    
    """
        Card History Utilities
    """
    def _saveCard(self) -> bool:
        """
            Saves current card if it has data (is not blank)
        """

        evidence_data = self._toHTML()

        # Create Card
        card = Card(
            self.warrant.text(),
            self.cite.text(),
            self.creds.text(),
            self.link.text(),
            evidence_data[0],
            evidence_data[1]
        )

        # Return if card has no data (avoid saving blank cards to .json)
        if not card.isCard():
            return
        
        if self.index is None:
            data.addCard(card)
        
        else:
            data.addCard(card, idx = self.index)
        
        return

    def _loadCard(self):
        """
            Loads most recent card
        """

        # Get index of most recent card
        self.index = data.getIndex()
        
        # Clear Fields
        document = self.evidence_box.document()
        document.clear()

        # If we don't have a previous card -> Set all fields as empty and return
        if self.index is None:
            self.warrant.setText("")
            self.cite.setText("")
            self.creds.setText("")
            self.link.setText("")
            return
        
        # If we do have a card, get it and set all the respective attrs in the GUI
        card = data.getCard(self.index)

        self.warrant.setText(card.TAG)
        self.cite.setText(card.CITE)
        self.creds.setText(card.CREDS)
        self.link.setText(card.URL)

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
            self.msg.setText("Card deleted successfully!")
            self.hasClickedDeleteOnce = False

        else:
            
            # If the card in Card Selector isn't what is actually open, alert user.
            if self.cards.currentText()[0] != self.index:
                self.msg.setHtml("""<b>WARNING! You are attempting to delete the card that is currently open,
                NOT what may be selected in the Card History bar. If you want to proceed, click the delete
                button again.</b>""")
            
            else:
                self.msg.setText("""You are attempting to delete the currently open card.
                Click the delete button again to confirm.""")
            
            self.hasClickedDeleteOnce = True
    
    def _cardSelectionChanged(self):
        """
            Resets the delete status (clicked once) if the selected card changes
            Saves any changes to the card
        """
        
        self._saveCard()
        self.hasClickedDeleteOnce = False

    """
        Shortcut Functions
    """
    def _autoCiteAndPoll(self):
        """
            Adds MLA & Debate-Grade Citation & article text to evidence box
        """

        self._auto(True, False)

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

        # Getting Current User's Home Dir
        startingDir = os.path.expanduser("~")

        # Getting input for target dir
        destDir = QFileDialog.getExistingDirectory(None,
                'Folder To Save In',
                startingDir,
                QFileDialog.ShowDirsOnly)
        
        # Getting HTML, filename
        html = self._toHTML()[1]
        filename = self.warrant.text() if self.warrant.text() != "" else "card"
        filepath = destDir + '/' + filename + '.pdf'

        try:
            ... # make pdf fxn
        
        except Exception:
            pass

    def _closeWindow(self):
        """
            Closes Window
        """

        self.close()

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

    def _highlightP(self):
        """
            Highlights text with Primary Highlight Color
        """
        
        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        HTML = f"<span style='background-color: {self.Primary_Highlight_Color}'>{selection_data[1]}</span>"
        self.__addText(HTML, selection_data[0])

    def _highlightS(self):
        """
            Highlights text with Secondary Highlight Color
        """

        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        HTML = f"<span style='background-color: {self.Secondary_Highlight_Color}'>{selection_data[1]}</span>"
        self.__addText(HTML, selection_data[0])

    def _bold_(self):
        """
            Bolds selected text
        """

        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        self.__addText(self._bold(selection_data[1]), selection_data[0])
    
    def _underline_(self):
        """
            Underlines selected text
        """

        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        self.__addText(self._underline(selection_data[1]), selection_data[0])

    def _italic_(self):
        """
            Italicises selected text
        """

        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        self.__addText(self._italic(selection_data[1]), selection_data[0])

    def _clearFormatting(self):
        """
            Clears Formatting on selected text
        """ 
        
        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        cursor = self.evidence_box.textCursor()
        cursor.insertText(selection_data[1])

    def _minimizeText(self):
        """
            Minimizes Text 
        """

        selection_data = self.__getSelectedText()
        if selection_data == None:
            return
        HTML = f'<span style="font-size: {self.Font_Size_Min}pt;">{selection_data[1]}</span>'
        self.__addText(HTML, selection_data[0])

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
    data.init()
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.light(app)
    gui = main(isLight=True)
    gui = qtmodern.windows.ModernWindow(gui)
    gui.show()
    sys.exit(app.exec_())