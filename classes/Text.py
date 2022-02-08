from typing import List
# from enums.Form import Form
from Paragraph import Paragraph

class Text:

    def __init__(self, text: str, form):
        self.text = text
        self.paragraphs = get_paragraphs()
        self.form = form

    def get_paragraphs(self) -> List[Paragraph]:
        pass

