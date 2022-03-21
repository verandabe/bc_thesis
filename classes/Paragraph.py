from typing import List

from utils import sentence_segment

from Protagonist import Protagonist
from Sentence import Sentence
from anaph import Anaph


class Paragraph:
    """
    Class representing a paragraph in a text to be rephrased.
    """

    def __init__(self, par_text: str, protg: Protagonist):
        self.text = par_text
        self.protg = protg
        self.anaphors: dict = Anaph.resolve(self.text)
        self.sentences = self._create_sentences()
        self.new_paragraph = self.text

    def _create_sentences(self) -> List[Sentence]:
        text_sentences = sentence_segment(self.text)
        object_sentences = []
        for s in text_sentences:
            sentence = Sentence(s, self.anaphors[s], self.protg)
            object_sentences.append(sentence)
        return object_sentences




