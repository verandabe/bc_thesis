from typing import List

from Forms import Form

from Paragraph import Paragraph
from Protagonist import Protagonist


class Text:
    """
    Class representing the text to be rephrased.
    """

    def __init__(self, text: str, form: Form, protg: Protagonist):
        self.text = text
        self.form = form
        self.protg = protg
        self.paragraphs = self._create_paragraphs()

    def _create_paragraphs(self) -> List[Paragraph]:
        text_paragraphs = self.text.split('\n')
        object_paragraphs = []
        for p in text_paragraphs:
            paragraph = Paragraph(p, self.protg)
            object_paragraphs.append(paragraph)
        return object_paragraphs

    def resolve_anaphors(self):  # TODO
        pass
