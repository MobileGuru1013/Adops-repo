"""
pdf file reader
"""
import PyPDF2
from Config import Config
from LogFile import logger
# import sys


class PdfReader(Config):

        def __init__(self):
            super(PdfReader, self).__init__()
            # super(PdfReader, self).config_logger()
            self.pdfFileobject = None
            self.pdf_Reader = None
            self.page_obj = None

        def file_object(self):
            file_object = open(self.section_value[2] + 'Mazda Document.pdf', 'rb')
            self.pdfFileobject = file_object

        def file_reader(self):
            pdf_reader = PyPDF2.PdfFileReader(self.pdfFileobject)
            self.pdf_Reader = pdf_reader

        def page_object(self):
            page_obj = self.pdf_Reader.getPage(0)
            page_content = page_obj.extractText()
            print(page_content)

        def main(self):
            logger.info('ssss')
            self.file_object()
            self.file_reader()
            self.page_object()


if __name__ == '__main__':
    object_pdf = PdfReader()
    object_pdf.main()



