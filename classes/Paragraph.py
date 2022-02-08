from typing import List
from Sentence import Sentence

class Paragraph:

    def __init__(self, par_text: str):
        self.text = par_text
        self.sentences = get_sentences()


    def get_sentences(self) -> List[Sentence]:
        pass

