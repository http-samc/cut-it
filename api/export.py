from sys import path
from resources.converter.xhtml2pdf import pisa
#from xhtml2pdf import pisa             
from docx import Document
from htmldocx import HtmlToDocx

class make:

    @staticmethod
    def docx(html, filename):

        document = Document()

        new_parser = HtmlToDocx()

        new_parser.add_html_to_document(html, document)

        document.save(filename)

    @staticmethod
    def pdf(html, filename):
        
        if filename.endswith('.pdf') == False:
            html += '.pdf'

        return make.convert_html_to_pdf(html, filename)

    @staticmethod
    def convert_html_to_pdf(source_html, output_filename):

        result_file = open(output_filename, "w+b")

        pisa_status = pisa.CreatePDF(
                source_html,                
                dest=result_file)           

        result_file.close()                 

        if pisa_status.err == None:
            return True

        else:
            return False
