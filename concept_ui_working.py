from PyQt5.QtWidgets import (QMainWindow, QPlainTextEdit, QApplication, QShortcut, QWidget)
from PyQt5 import QtCore, QtGui, QtWidgets
from klembord import Selection
from api.QComboBoxPlus import ExtendedComboBox
from api.clipboard_WIN import clipboard 
from PyQt5.QtWidgets import QFileDialog
from api.feedback import send_feedback
from api.export import make, PrintPDF
from api.settings import Settings
from api.QBrowser import Browser
from api.auth_tools import tools
from bs4 import BeautifulSoup
from api.resource import PATH
from api.version import check
from PyQt5.QtCore import *
from api.citer import cite
from api.texter import text
from api.texter import news
from api.data import store
import sys
import os
from PyQt5 import uic
import qtmodern.windows
import qtmodern.styles

global settings 
settings = Settings()

class GUI(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        # Loading UI
        uic.loadUi('modern_ui.ui', self)
    
        # Setting Title
        self.setWindowTitle("Cut-It™ by Offtime Roadmap® v.0.5.1@beta")

        # Setting Close Event
        self.closeEvent = self.onClose

        # Setting Slots

            # Custom Emphasis Levels
        self.cutit_button.clicked.connect(self.primary_emphasis)
        self.secondary.clicked.connect(self.secondary_emphasis)
        self.tertiary.clicked.connect(self.tertiary_emphasis)

            # Generic Styling 
        self.bold_button.clicked.connect(self.bold_)
        self.underline_button.clicked.connect(self.underline_)
        self.italic_button.clicked.connect(self.italic_)
        self.highlight_p_button.clicked.connect(self.highlightP)
        self.highlight_s_button.clicked.connect(self.highlightS)

            # Misc
        self.copy_button.clicked.connect(self.copy)
        self.autocut.clicked.connect(self.autocut_)
        self.settings_button.clicked.connect(self.settings)

        # Signals
        self.evidence_box.textChanged.connect(self.addDelimiter)
        # Other __init__ reqs
        self.shortcuts()
        self.index=None
        #self.selectCard() TODO

    def addDelimiter(self):
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

    def highlightP(self):
        return None

    def highlightS(self):
        return None

    def openNewCard(self):
        return None

    def settings(self):
        return None

    def copy(self):
        data = self.toHTML()
        clipboard.add(data[0], data[1])  

    """
    generic emphasis
    """

    def bold_(self):
        self.generic_emphasis(bold=True)
    
    def underline_(self):
        self.generic_emphasis(underline=True)
    
    def italic_(self):
        self.generic_emphasis(italic=True)
    
    def highlightP(self):
        self.generic_emphasis(PH=True)
    
    def highlightS(self):
        self.generic_emphasis(SH=True)

    def generic_emphasis(self, bold: bool = False, italic: bool = False, underline: bool = False, PH: bool = False, SH: bool = False):
        
        cursor = self.evidence_box.textCursor()
        if cursor.hasSelection() == False:
            return None
        
        START = cursor.selectionStart()

        selection = cursor.selectedText()
        config = settings.PES()

        selection = self.italic(selection) if italic else selection
        selection = self.bold(selection) if bold else selection
        selection = self.underline(selection) if underline else selection
        selection = self.highlight(selection, settings.PHC(), settings.FSNT()) if PH else selection
        selection = self.highlight(selection, settings.SHC(), settings.FSNT()) if SH else selection
        
        cursor.insertHtml(selection)
        cursor.setPosition(START, QtGui.QTextCursor.KeepAnchor)
        self.evidence_box.setTextCursor(cursor)

        data = self.toHTML()
        clipboard.add(data[0], data[1])

    """
    emphasis levels
    """
    def primary_emphasis(self):
        """
        Formats using Primary emphasis
        """

        cursor = self.evidence_box.textCursor()
        if cursor.hasSelection() == False:
            return None
        
        START = cursor.selectionStart()

        selection = cursor.selectedText()
        config = settings.PES()

        #selection = self.border(selection)
        selection = self.italic(selection) if config[0] else selection
        selection = self.bold(selection) if config[1] else selection
        selection = self.underline(selection) if config[2] else selection
        selection = self.highlight(selection, settings.PHC(), settings.FSPE()) if config[3] else self.size(selection, settings.FSPE())
        
        cursor.insertHtml(selection)
        cursor.setPosition(START, QtGui.QTextCursor.KeepAnchor)
        self.evidence_box.setTextCursor(cursor)

        data = self.toHTML()
        clipboard.add(data[0], data[1])

    def secondary_emphasis(self):
        """
        Formats using Secondary emphasis
        """

        cursor = self.evidence_box.textCursor()
        if cursor.hasSelection() == False:
            return None

        START = cursor.selectionStart()

        selection = cursor.selectedText()
        config = settings.SES()

        selection = self.italic(selection) if config[0] else selection
        selection = self.bold(selection) if config[1] else selection
        selection = self.underline(selection) if config[2] else selection
        selection = self.highlight(selection, settings.SHC(), settings.FSNT()) if config[3] else self.size(selection, settings.FSNT())
        
        cursor.insertHtml(selection)
        cursor.setPosition(START, QtGui.QTextCursor.KeepAnchor)
        self.evidence_box.setTextCursor(cursor)

        data = self.toHTML()
        clipboard.add(data[0], data[1])

    def tertiary_emphasis(self):
        """
        Formats using Tertiary emphasis
        """

        cursor = self.evidence_box.textCursor()
        if cursor.hasSelection() == False:
            return None
        
        START = cursor.selectionStart()

        selection = cursor.selectedText()
        config = settings.TES()

        selection = self.italic(selection) if config[0] else selection
        selection = self.bold(selection) if config[1] else selection
        selection = self.underline(selection) if config[2] else selection
        selection = self.highlight(selection, settings.SHC(), settings.FSNT()) if config[3] else self.size(selection, settings.FSNT())
        
        cursor.insertHtml(selection)
        cursor.setPosition(START, QtGui.QTextCursor.KeepAnchor)
        self.evidence_box.setTextCursor(cursor)

        data = self.toHTML()
        clipboard.add(data[0], data[1])

    """
    styling methods
    """
    def border(self, html):
        """
        adds border to selected text
        """

        return f'<span style="border-style:solid;">{html}</span>'

    def italic(self, html):
        """
        italicises selected text
        """
             
        return f"<em>{html}</em>"
    
    def bold(self, html):
        """
        adds html bolding to str
        """
   
        return f"<b>{html}</b>"

    def underline(self, html):
        """
        adds html underlining to str
        """  

        return f"<u>{html}</u>"
        
    def highlight(self, html, color, font_size):
        """
        adds html highlighting to str
        """
        return f"<span style='background-color: {color}; font-size: {font_size}pt;'>{html}</span>"

    def size(self, html, font_size):
        """
        adds html font resizing to str
        """
        return f"<span style='font-size: {font_size}pt;'>{html}</span>"

    def shortcuts(self):
        """
            Inits custom keybindings for all user-defined shortcuts
        """

        # CF DONE
        CF = QShortcut(QtGui.QKeySequence('Ctrl+Z'), self.evidence_box)
        CF.activated.connect(self.clearFormatting)

        # Find
        KST = QShortcut(QtGui.QKeySequence('Ctrl+F'), self.evidence_box)
        KST.activated.connect(self.find)
        self.cursor_find = self.evidence_box.textCursor()

        # KST TODO
        KST = QShortcut(QtGui.QKeySequence(settings.KST()), self.evidence_box)
        KST.activated.connect(self.keepSelectedText)

        # PE DONE
        PE = QShortcut(QtGui.QKeySequence(settings.PE()), self.evidence_box)
        PE.activated.connect(self.primary_emphasis)

        # SE DONE

        SE = QShortcut(QtGui.QKeySequence(settings.SE()), self.evidence_box)
        SE.activated.connect(self.secondary_emphasis)

        # TE DONE

        TE = QShortcut(QtGui.QKeySequence(settings.TE()), self.evidence_box)
        TE.activated.connect(self.tertiary_emphasis)

        # MT DONE

        MT = QShortcut(QtGui.QKeySequence(settings.MT()), self.evidence_box)
        MT.activated.connect(self.MT)

        # AP DONE

        AP = QShortcut(QtGui.QKeySequence(settings.AP()), self.evidence_box)
        AP.activated.connect(self.AP)

        # AC DONE

        AC = QShortcut(QtGui.QKeySequence(settings.AC()), self.evidence_box)
        AC.activated.connect(self.AC)

        # AP_AC DONE

        AP_AC = QShortcut(QtGui.QKeySequence(settings.AP_AC()), self.evidence_box)
        AP_AC.activated.connect(self.AP_AC)

        # PDF DONE

        PDF = QShortcut(QtGui.QKeySequence(settings.PDF()), self.evidence_box)
        PDF.activated.connect(self.print)

        # NC

        NC = QShortcut(QtGui.QKeySequence(settings.IP()), self.evidence_box)
        NC.activated.connect(self.openNewCard)

        # OS DONE

        OS = QShortcut(QtGui.QKeySequence(settings.OS()), self.evidence_box)
        OS.activated.connect(self.settings)

        # CW DONE

        CW = QShortcut(QtGui.QKeySequence(settings.CW()), self.evidence_box)
        CW.activated.connect(self.quit_)

    def loadLight(self):
        """
            Specific theme overrides for Light mode
        """

        self.evidence_box.setStyleSheet("background-color: rgb(220,220,220);\n")

    def toHTML(self):
        """
            Returns HTML rep. of card
        """

        doc = self.evidence_box.document()
        soup = BeautifulSoup(doc.toHtml(), 'html.parser')
        html = str(soup.find('p'))
        html = html.replace('600', 'bold')
        html = f'<body style="font-family: {settings.font()}">' + html + '</body>'
        text = str(soup.text)
        return [text, html]

    def autocut_(self):
        """
            Uses user defined button to autocut
        """

        self.auto(False, False) 

    def keepSelectedText(self):
        # TODO Implement
        return None

    def clearFormatting(self):
        cursor  = self.evidence_box.textCursor()
        if cursor.hasSelection() == False:
            return None
        selection_plain = cursor.selectedText()
        cursor.insertText(selection_plain)

    def MT(self):
        
        cursor = self.evidence_box.textCursor()
        if cursor.hasSelection() == False:
            return None
        selection = cursor.selectedText()
        
        selection = self.size(selection, settings.FSMT())
        cursor.removeSelectedText()        
        cursor.insertHtml(selection)
        
        data = self.toHTML()
        clipboard.add(data[0], data[1])

    def AC(self):
        self.auto(True, False)

    def AP(self):
        self.auto(False, True)   
    
    def AP_AC(self):
        self.auto(True, True)

    def print(self):
        
        # Getting Current Dir
        startingDir = os.getcwd()

        # Getting User Input for Target Dir
        destDir = QFileDialog.getExistingDirectory(None, 
                'Folder To Save In', 
                startingDir, 
                QFileDialog.ShowDirsOnly)

        # Getting HTML, filename
        html = self.toHTML()[1] 
        filename = destDir + '/' + self.warrant_input.text() + '.pdf'
        # Making PDF

        if filename != "/.pdf":
            try:
                self.widget = QWidget()
                self.browser = PrintPDF(html, filename)
                self.browser.setupUi(self.widget)
            
            except Exception:
                pass

    def find(self):
        # TODO: implement w/ extraselections
        return None        
        # document = self.evidence_box.document()
        # if self.cursor_find.hasSelection():
        #     FROM = self.cursor_find.selectionEnd()
        # else:
        #     FROM = 0
        # self.cursor_find = document.find("the", FROM)
        # self.evidence_box.setTextCursor(self.cursor_find)

    def auto(self, autoCite, autoPoll):
        """
        Takes in 2 bools that can override the state of the checkboxes for each option,
        then executes them
        """

        URL = self.link_input.text()
        
        citation = f"""
        <p>
        """

        # If both Poll/Cite enabled
        if (self.autocite_box.isChecked() is True or autoCite is True) and (self.autopoll_box.isChecked() is True or autoPoll is True):

            #De-checking both boxes
            self.autocite_box.setCheckState(False)
            self.autopoll_box.setCheckState(False)

            #Inputting Cite
            CREDS = self.creds_input.text()
            TAG = self.warrant_input.text()

            c = cite(URL)
            citation_data_debate = c.debate()
            citation_mla = c.mla()

            if TAG != "":
                citation += f"""
                <span style='background-color: yellow; font-size: 12pt;'><u><strong>
                    {TAG}
                </strong></u></span><br>
                """
            
            citation += f"""
            <span style='background-color: cyan; font-size: 12pt;'><u><strong>
                {citation_data_debate[0]} '{citation_data_debate[1]}<br>
            </strong></u></span>
            """

            if CREDS != "":
                citation += f"""
                <i>
                {CREDS}<br>
                </i>
                """

            citation += f"""
            {citation_data_debate[2]} • {citation_data_debate[3]}<br>
            {citation_mla}<br><br>
            """

            #Inputting Article Text
            if "nytimes.com" in URL:
                article = text.get(URL)
            else:
                article = news.paper(URL)
            citation += article + "</p>"

            #Inserting Text
            cursor = self.evidence_box.textCursor()
            cursor.setPosition(0)
            cursor.insertHtml(citation)  

            return True

        #AutoCite checked Only
        elif (self.autocite_box.isChecked() is True) or (autoCite is True):
            
            #De-checking box
            self.autocite_box.setCheckState(False)

            #Inputting Cite
            CREDS = self.creds_input.text()
            TAG = self.warrant_input.text()

            c = cite(URL)
            citation_data_debate = c.debate()
            citation_mla = c.mla()

            if TAG != "":
                citation += f"""
                <span style='background-color: yellow; font-size: 12pt;'><u><strong>
                    {TAG}
                </strong></u></span><br>
                """
            
            citation += f"""
            <span style='background-color: cyan; font-size: 12pt;'><u><strong>
                {citation_data_debate[0]} '{citation_data_debate[1]}<br>
            </strong></u></span>
            """

            if CREDS != "":
                citation += f"""
                <i>
                {CREDS}<br>
                </i>
                """

            citation += f"""
            {citation_data_debate[2]} • {citation_data_debate[3]}<br>
            {citation_mla}<br><br>
            </p>
            """

            #Inserting Text
            cursor = self.evidence_box.textCursor()
            cursor.setPosition(0)
            cursor.insertHtml(citation) 
            
            return True

        #Autopoll Checked Only
        elif (self.autopoll_box.isChecked() is True) or (autoPoll is True):
            
            #De-checking box
            self.autopoll_box.setCheckState(False)

            #Getting article, inputting it
            if "nytimes.com" in URL:
                article = text.get(URL)
            else:
                article = news.paper(URL)
            citation += article + "</p>"

            #Inserting Text
            cursor = self.evidence_box.textCursor()
            cursor.setPosition(0)
            cursor.insertHtml(citation)  

            return True

        else:
            return False  

    def quit_(self):
        if settings.LI() == False:
            store.log_out()
        quit()

    def onClose(self, event):
        """
            Behavior for window close (saves card)
        """   

        evidence_data = self.toHTML()
        tag = self.warrant_input.text()
        cite = self.cite_input.text()
        creds = self.creds_input.text()
        link = self.link_input.text()

        card = {
            "tag" : tag,
            "cite" : cite,
            "creds" : creds,
            "link" : link,
            "html" : evidence_data[1],
            "text" : evidence_data[0]
        }

        if self.index is None:
            store.addCard(card)

        else:
            store.updateCard(card, self.index)

        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.dark(app)
    gui = GUI()
    gui = qtmodern.windows.ModernWindow(gui)
    gui.show()
    sys.exit(app.exec_())