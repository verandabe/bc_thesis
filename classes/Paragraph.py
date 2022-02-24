from typing import List
from Sentence import Sentence

class Paragraph:
    """
    Class representing a paragraph in a text to be rephrased.
    """

    def __init__(self, par_text: str):
        self.text = par_text
        self.sentences = self.get_sentences()

    def get_sentences(self) -> List[Sentence]:
        pass

