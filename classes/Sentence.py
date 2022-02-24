from typing import List, Dict
from Word import Word
from syn import Syn


class Sentence:
    """
    Class object representing a sentence
    """

    def __init__(self, sentence: str, anaphors: Dict[str, str]):
        # self.nodes = Syn.get_sentence_nodes(sentence)
        self.words = None # TODO
        self.root = None # TODO
        self.anaphors = anaphors
        # self.resolved_subject =

    def get_words(self) -> List[Word]:
        # nodes -> words
        pass

    def get_root(self):
        # nodes -> ... root
        pass

