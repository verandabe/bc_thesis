from typing import List
import re

from utils import sentence_segment

from Protagonist import Protagonist
from Sentence import Sentence
from anaph import Anaph


class Paragraph:
    """
    Class representing a paragraph in a text to be rephrased.
    """

    def __init__(self, par_text: str, protg: Protagonist):
        self.text = self.preprocess_direct_speech(par_text)
        self.protg = protg
        self.anaphors: dict = Anaph.resolve(self.text)
        self.sentences = self._create_sentences()
        self.new_paragraph = self.text

    def _create_sentences(self) -> List[Sentence]:
        text_sentences = sentence_segment(self.text)
        object_sentences = []
        for s in text_sentences:
            added = False

            for sent_anaph in self.anaphors:
                if sent_anaph in s[:-1]:
                    sentence = Sentence(s, self.anaphors[sent_anaph], self.protg)
                    added = True
            if not added:
                sentence = Sentence(s, {}, self.protg)
            object_sentences.append(sentence)
        return object_sentences

    def preprocess_direct_speech(self, text):
        pattern = r'[„][^„“]*[“]'

        def direct_repl(matchobj):
            repl = matchobj.group(0).replace(" ", "_")
            return repl

        prepared_par = re.sub(pattern, direct_repl, text)
        return prepared_par


