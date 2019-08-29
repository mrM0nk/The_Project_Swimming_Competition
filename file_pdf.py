import fitz


class Pdf:

    def __init__(self, file_name):
        self.pdf = fitz.open(file_name)

    def get_content(self):
        pages = [self.pdf[namber] for namber in range(self.pdf.pageCount)]
        content = [page.getTextBlocks(images=False) for page in pages]
        return content