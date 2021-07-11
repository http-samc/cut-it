"""
    Creates a GUI object based off the latest version of app.ui
    GUI visual tests can be ran by running this program
    Inherited by app.py for simplicity
"""

import sys

import qtmodern.styles
import qtmodern.windows
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QFrame, QLabel, QLayout, QMainWindow

from utils.distro import tag, version
from utils.ext_combobox import ExtendedComboBox
from utils.MainWindow import MainWindow
from utils.resource import PATH

class GUI(MainWindow): # QMainWindow for test, MainWindow for Build

    def __init__(self, isLight = False) -> None:
        """
            Loads latest UI
        """

        super().__init__()

        # Storing theme
        self.isLight = isLight

        self.setWindowIcon(QtGui.QIcon(PATH.get('images/cut-it.ico')))

        # Loading UI
        #uic.loadUi('Cut-It/app.ui', self)

        # Setting Title (Spaces are due to a centering bug in QtModern)
        SPACES = "                    "
        self.setWindowTitle(f"{SPACES}Cut-It™ v.{version()}@{tag()}")

        # Applying custom changes to GUI
        self.addDistroDetails()
        self.addCardHistory()
        self.addAttrs()
        self.addToolTips()
        self.updateStyling()

    def addCardHistory(self):
        """
            Manually fill out the Card History groupBox (due to custom widgets)
        """

        self.gridLayout_7.setSpacing(5)
        self.cardSelector = ExtendedComboBox()
        self.cardSelector.setObjectName(u"cardSelector")
        self.cardSelector.setMinimumSize(QSize(230, 20))
        self.gridLayout_7.addWidget(self.cardSelector, 0, 0, 1, 3)

        self.open_card = QtWidgets.QPushButton()
        self.open_card.setObjectName(u"open_card")
        self.open_card.setMinimumSize(QSize(100, 20))
        self.open_card.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayout_7.addWidget(self.open_card, 0, 3)

        self.delete_card = QtWidgets.QPushButton()
        self.delete_card.setObjectName(u"delete_card")
        self.delete_card.setMinimumSize(QSize(70, 20))
        self.delete_card.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayout_7.addWidget(self.delete_card, 1, 0)

        self.copy_card = QtWidgets.QPushButton()
        self.copy_card.setObjectName(u"copy")
        self.copy_card.setMinimumSize(QSize(70, 20))
        self.copy_card.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayout_7.addWidget(self.copy_card, 1, 1)

        self.save_card = QtWidgets.QPushButton()
        self.save_card.setObjectName(u"save_card")
        self.save_card.setMinimumSize(QSize(70, 20))
        self.save_card.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayout_7.addWidget(self.save_card, 1, 2)

        self.new_card = QtWidgets.QPushButton()
        self.new_card.setObjectName(u"new_card")
        self.new_card.setMinimumSize(QSize(100, 20))
        self.new_card.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayout_7.addWidget(self.new_card, 1, 3)

    def updateStyling(self):
        # Set theme-appropriate tooltip background and evidence box color
        if self.isLight:
            self.setStyleSheet("QToolTip { color: #616161; background-color: #f2f2f2; border: 0px;}")
        else:
            self.setStyleSheet("QToolTip { color: #f2f2f2; background-color: #616161; border: 0px;}")

    def addToolTips(self):
        """
            Adds in ToolTips
        """

        # Adding ToolTips
        self.warrant.setToolTip("""
        The <code>Tagline</code> is where you can input a shorthand name/summary for the card<br><br>
        - This gets inserted at the top of the card when you use <code>AutoCut</code>, but you need to enter it beforehand<br><br>
        - If you save the card, this is required and will become the PDF's filename
        """)
        self.creds.setToolTip("""
        The <code>Credentials</code> is where you can input the credentials of the source of your card<br><br>
        - This gets inserted within the citation when you use <code>AutoCut</code>, but you need to enter it beforehand
        """)
        self.link.setToolTip("""
        The <code>URL</code> is where you can input the URL of the card, which can be a webpage or a YouTube video<br><br>
        - This this is used by <code>AutoCut</code> to get the citation and poll text<br><br>
        - If you input a YouTube video, the captions are used as article text
        """)
        self.autocite.setToolTip("""
        <code>AutoCite</code> allows you to auto-generate a debate-grade and MLA citation from the link you inputted in <code>URL</code><br><br>
        - If this is checked, it is triggered when you click <code>AutoCut</code> to the right
        """)
        self.autopoll.setToolTip("""
        <code>AutoPoll</code> allows you to auto-insert the text of the webpage you inputted in <code>URL</code><br><br>
        - If this is checked, it is triggered when you click <code>AutoCut</code> to the right
        - If you entered a YouTube Video, the captions are used as article text
        """)
        self.autocut.setToolTip("""
        <code>AutoCut</code> is a feature that saves time getting card details!<br><br>
        - If the <code>AutoCite</code> checkbox (to the left) is activated, it will add an MLA &
        Debate-style citation to your card.<br><br>
        - If the <code>AutoPoll</code> checkbox to the left is activated, it will add the text
        of the website to your card.<br><br>
        - You need to select which (or both) of these options you want prior to
        clicking the button.<br><br>
        - Make sure you enter any card details in the
        <code>Card Information</code> section prior to AutoCutting - <em>they won't fill in afterwards</em>!
        """)
        self.primary_em.setToolTip("""
        <code>Primary Emphasis</code> allows you to quickly format the selected text in the <code>Evidence Box</code><br><br>
        - The formatting used is determined by what's selected in the <code>Settings</code> tab<br><br>
        - This can also be accessed by a shortcut that you've defined in the <code>Settings</code> tab
        """)
        self.secondary_em.setToolTip("""
        <code>Secondary Emphasis</code> allows you to quickly format the selected text in the <code>Evidence Box</code><br><br>
        - The formatting used is determined by what's selected in the <code>Settings</code> tab<br><br>
        - This can also be accessed by a shortcut that you've defined in the <code>Settings</code> tab
        """)
        self.tertiary_em.setToolTip("""
        <code>Tertiary Emphasis</code> allows you to quickly format the selected text in the <code>Evidence Box</code><br><br>
        - The formatting used is determined by what's selected in the <code>Settings</code> tab<br><br>
        - This can also be accessed by a shortcut that you've defined in the <code>Settings</code> tab
        """)
        self.bold.setToolTip("""
        <code>Bold</code> allows you to quickly bold the selected text in the <code>Evidence Box</code><br><br>
        """)
        self.underline.setToolTip("""
        <code>Underline</code> allows you to quickly underline the selected text in the <code>Evidence Box</code><br><br>
        """)
        self.italics.setToolTip("""
        <code>Italics</code> allows you to quickly italicise the selected text in the <code>Evidence Box</code><br><br>
        """)
        self.primary_highlight.setToolTip("""
        <code>Primary Highlight</code> allows you to quickly highlight the selected text in the <code>Evidence Box</code><br><br>
        - The highlight color used is determined by what you selected for <code>Highlight #1</code> in the <code>Settings</code> tab
        """)
        self.secondary_highlight.setToolTip("""
        <code>Secondary Highlight</code> allows you to quickly highlight the selected text in the <code>Evidence Box</code><br><br>
        - The highlight color used is determined by what you selected for <code>Highlight #2</code> in the <code>Settings</code> tab
        """)
        self.minimize.setToolTip("""
        <code>Minimize</code> allows you to quickly minimize the selected text in the <code>Evidence Box</code><br><br>
        - The minimized font-size used is determined by what you selected for <code>Font Size of Minimized Text</code> in the <code>Settings</code> tab<br><br>
        - This can also be accessed by a shortcut that you've defined in the <code>Settings</code> tab
        """)
        self.clearSelectionFormatting.setToolTip("""
        <code>Clear Selection Formatting</code> allows you to clear any emphasis you have applied to your selected text in the <code>Evidence Box</code><br><br>
        - This can also be accessed by a shortcut defined in <code>Settings</code>
        """)
        self.new_card.setToolTip("""
        The <code>New Card</code> button allows you to open a new card to cut<br><br>
        - Any currently opened work is autosaved to be accessed later in the <code>Card Selector</code><br>
        - You can access previous cards in the <code>Card Selector</code>
        """)
        self.cardSelector.setToolTip("""
        The <code>Card Selector</code> allows you to reaccess any card you've ever cut with Cut-It!<br><br>
        - Once you want to view a different card, select the option and click the open button (first one to the right);
        the different/new card will be opened, and the one you were working on will be autosaved and added to the list<br><br>
        - There is no dedicated save button - everything is saved automatically (even if you shut down the program)<br><br>
        - You can also type into the box to search for a card
        """)
        self.open_card.setToolTip("""
        The <code>Open Card</code> button allows you to open the currently opened card (or cut a new card if applicable)<br><br>
        - Your previous card is automatically saved
        """)
        self.delete_card.setToolTip("""
        The <code>Delete Card</code> button allows you to permanently delete a card from your Card History<br><br>
        - This feature goes off the card that is currently opened, <b>not</b> what is selected in the Card Selector. You need to use the <code>Open Card</code>
        button to open the selected card first, or else the currently opened card will be deleted and <b>not</b> what you've selected in the <code>Card Selector</code><br><br>
        - You need to click it twice to delete any particular card
        """)
        self.copy_card.setToolTip("""
        The <code>Copy Card</code> button allows you to copy the currently opened card to your clipboard<br><br>
        - This feature goes off the card that is currently opened, <b>not</b> what is selected in the Card Selector. You need to use the <code>Open Card</code>
        button to open the selected card first, or else the currently opened card will be copied and <b>not</b> what you've selected in the <code>Card Selector</code><br><br>
        - This should only be used when reaccessing any old cards, becuase anytime you change a card it's automatically copied to your clipboard<br><br>
        - Remember to never manually select text from the Evidence Box, not only is it slower but formatting will be lost (which means you can't use it with Docs/Word)
        """)
        self.save_card.setToolTip("""
        The <code>Save Card</code> button allows you to save the currently opened card as a PDF<br><br>
        - This feature goes off the card that is currently opened, <b>not</b> what is selected in the Card Selector. You need to use the <code>Open Card</code>
        button to open the selected card first, or else the currently opened card will be saved and <b>not</b> what you've selected in the <code>Card Selector</code><br><br>
        - You need to enter a Tagline (which becomes the filename), or the file will be called card.pdf""")
        self.msg.setToolTip("""
        The <code>Message</code> box alerts you of what the program is doing at any given moment.
        """)
        self.font.setToolTip("The font that will be used when copying/saving your cards (applies on restart)")
        self.font_size_normal.setToolTip("This is the font size for normal, non-emphasized text (applies on restart)")
        self.font_size_min.setToolTip("This is the font size for minimized text (applies on restart)")
        self.font_size_normal.setToolTip("This is the font size for normal, non-emphasized text (applies on restart)")
        self.zoom.setToolTip("""
        This will increase the zoom on the evidence box. Your cards will still export the same with the autocopy feature or the copy button (applies on restart)<br><br>
        - <u><b>Remember to never copy the text in the evidence box manually, since it won't work with Docs/Word. AutoCut automatically copies
        text to your clipboard anytime you change a card, and it's faster!</b></u>""")
        self.highlight_1.setToolTip("This is the highlight color you can use to highlight text with the <code>H¹</code> button (applies on restart)")
        self.highlight_2.setToolTip("This is the highlight color you can use to highlight text with the <code>H²</code> button (applies on restart)")

        self.primary_bold.setToolTip("Defines whether or not the Primary Emphasis level bolds text (applies on restart)")
        self.primary_underline.setToolTip("Defines whether or not the Primary Emphasis level underlines text (applies on restart)")
        self.primary_italicised.setToolTip("Defines whether or not the Primary Emphasis level italicises text (applies on restart)")
        self.primary_highlight_2.setToolTip("Defines whether or not the Primary Emphasis level highlights text (and what color it uses) (applies on restart)")
        self.primary_size.setToolTip("Defines the font size of the Primary Emphasis level (applies on restart)")

        self.secondary_bold.setToolTip("Defines whether or not the Secondary Emphasis level bolds text (applies on restart)")
        self.secondary_underline.setToolTip("Defines whether or not the Secondary Emphasis level underlines text (applies on restart)")
        self.secondary_italicised.setToolTip("Defines whether or not the Secondary Emphasis level italicises text (applies on restart)")
        self.secondary_highlight_2.setToolTip("Defines whether or not the Secondary Emphasis level highlights text (and what color it uses) (applies on restart)")
        self.secondary_size.setToolTip("Defines the font size of the Secondary Emphasis level (applies on restart)")

        self.tertiary_bold.setToolTip("Defines whether or not the Tertiary Emphasis level bolds text (applies on restart)")
        self.tertiary_underline.setToolTip("Defines whether or not the Tertiary Emphasis level underlines text (applies on restart)")
        self.tertiary_italicised.setToolTip("Defines whether or not the Tertiary Emphasis level italicises text (applies on restart)")
        self.tertiary_highlight.setToolTip("Defines whether or not the Tertiary Emphasis level highlights text (and what color it uses) (applies on restart)")
        self.tertiary_size.setToolTip("Defines the font size of the Tertiary Emphasis level (applies on restart)")

        self.shortcuts.setToolTip("Allows you to choose which shortcut you'd like to view and/or customize (changes apply on restart)")
        self.shortcut_input.setToolTip("Allows you to view the shortcut selected above. If you'd like to change it, click once and enter your new shortcut (changes apply on restart).")

        self.theme.setToolTip("Changes theme to opposite version (light -> dark; dark -> light)")
        self.feedback.setToolTip("Enter any feedback you have and submit it below")
        self.submit_feedback.setToolTip("Submit the feedback you entered above")
        self.evidence_box.setToolTip("This is where you cut your card!")

    def addAttrs(self):
        """
            Adds in missing attrs.
        """

        # Setting up message box
        self.msg.setCurrentFont(QtGui.QFont("Times New Roman"))
        self.msg.insertHtml("<p>Welcome to Cut-It! Hover over an item for a few seconds to get a description, or read the docs at: <b>docs.cutit.cards</b>!</p>")

        # Adding Icons
        self.autocut.setIcon(QtGui.QIcon(PATH.get('images/cut_icon.png')))
        self.new_card.setIcon(QtGui.QIcon(PATH.get('images/new_icon.png')))
        self.open_card.setIcon(QtGui.QIcon(PATH.get('images/open_icon.png')))
        self.delete_card.setIcon(QtGui.QIcon(PATH.get('images/delete_icon.png')))
        self.copy_card.setIcon(QtGui.QIcon(PATH.get('images/copy_icon.png')))
        self.save_card.setIcon(QtGui.QIcon(PATH.get('images/save_icon.png')))
        self.autobypass.setIcon(QtGui.QIcon(PATH.get('images/browser_icon.png')))

        # Setting Text
        self.open_card.setText(" Open Selection ")
        self.new_card.setText("    New Card      ")
        self.delete_card.setText(" Delete")
        self.copy_card.setText(" Copy")
        self.save_card.setText(" Export")

    def addDistroDetails(self) -> str:
        """
            Returns a formatted String to be inserted into the Distro box in the about section
        """

        distroDetails = f"""<h1 align="center" style="font-size: 30pt">🚀Cut-It FAQ🚀</h1><br><br><h1 align="center">
        Version 📝 {version()} || Tag🏷️ @{tag()}
        || Website🌐 https://cutit.cards || GitHub Repository📚 https://github.com/http-samc/cut-it
        || Contributors👐 https://github.com/http-samc/cut-it/graphs/contributors
        || Current Project Managers👷 Samarth Chitgopekar, Adithya Vaidyanathan, Gabriel Seidman
        """.replace('\n','') + "<br><br>Icon Credits (IconScout): Scissors Icon by Daniel Bruce, Save Icon by Google Inc., "
        distroDetails += "Delete Icon by Alex Martynov, Clipboard Icon by Soni Sokell, Open Window Icon by Benjamin Sperry, "
        distroDetails += "New Icon by Phosphor Icons, Browser Icon by Bawie Cahyo, Search Icon by Google Inc.</h1>"
        distroDetails += """
        <br><br>
        <h1 align="center">
        <em>
        See any issues? Contact us at hello@cutit.cards! Our software is free forever and open sourced,
        please consider contributing on GitHub!
        </em>
        <h1>
        """
        self.distro.setText(distroDetails)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    qtmodern.styles.dark(app)
    gui = GUI(isLight=False)
    gui = qtmodern.windows.ModernWindow(gui)
    gui.show()
    sys.exit(app.exec_())
