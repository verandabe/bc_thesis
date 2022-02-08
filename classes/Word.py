# from tools.morph import Morph # TODO path
# from enums.Member import Member
from typing import List

class Word:

    def __init__(self, string: str, member, dependers, anaphor, ds: bool):
        self.word = string
        # self.lemma = Morph.get_lemma(string) # TODO
        # self.tag = Morph.get_tag(string)
        self.member = member
        self.dependencies = dependers
        self.new_form = None
        self.anaphor = anaphor
        self.direct_speech = ds


    def generate_new_form(self) -> str: # TODO
        return self.word

