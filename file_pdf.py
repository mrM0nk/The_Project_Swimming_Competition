import fitz
from competition import Event


class Pdf:

    def __init__(self, file_name):
        self.pdf = fitz.open(file_name)

    def get_content(self):
        pages = [self.pdf[namber] for namber in range(self.pdf.pageCount)]
        content = [page.getTextBlocks() for page in pages]
        event_title = content[0][0][4].replace('\n', '') + content[0][1][4]
        third_row = content[0][2][4].split()
        event_date = third_row[0]
        event_location = third_row[3][:-1]
        event = Event(title=event_title, location=event_location, date=event_date)
        return content, event


    @classmethod
    def determine_what_type(cll):
        pass

class Pdf_first_type(Pdf):

    def __init__(self):
        super().__init__(self)
        self.type_of_pdf = 'first'






class Pdf_second_type(Pdf):
    type_of_pdf = 'second'
    pass


class Page:

    def __init__(self, namber):
        self.namber = namber


