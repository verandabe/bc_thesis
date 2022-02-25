from typing import List
from Sentence import Sentence
from Protagonist import Protagonist
from utils import sentence_segment

class Paragraph:
    """
    Class representing a paragraph in a text to be rephrased.
    """

    def __init__(self, par_text: str, protg: Protagonist):
        self.text = par_text
        self.protg = protg
        self.anaphors = {}  # TODO
        self.sentences = self._create_sentences()


    def _create_sentences(self) -> List[Sentence]:
        text_sentences = sentence_segment(self.text)
        object_sentences = []
        for s in text_sentences:
            sentence = Sentence(s, self.anaphors, self.protg)
            object_sentences.append(sentence)
        return object_sentences

    def resolve_anaphors(self):
        pass  # TODO




