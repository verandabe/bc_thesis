from morph import Morph
from Forms import Form
from Protagonist import Protagonist
from Members import Member
from icher_rules import *


class Word:
    """
    Class representing a word.
    """

    def __init__(self, index, string: str, member: Member, parent_idx, dependents, anaphor, ds: bool):
        self.index = index
        self.word = string
        self.lemmas = Morph.get_lemmas(string) # TODO
        self.tags = Morph.get_tags(string)
        # self.lts = Morph.get_lt(string)
        self.member = member
        self.parent_idx = parent_idx
        self.parent_node = None
        self.dependents = dependents
        self.new_form = string+"_new" # TODO delete after testing
        self.anaphor = anaphor
        self.direct_speech = ds

    def generate_new_form(self, form: Form, protg: Protagonist) -> str:  # TODO
        if not self.is_real_word() or self.direct_speech:
            return

        if form == Form.ICH:
            self._ich_to_er(protg)

        elif form == Form.ER:
            pass


    def is_real_word(self) -> bool:
        return "<" not in self.word

    def _ich_to_er(self, protg: Protagonist):
        for i in range(len(self.lemmas)):
            if (self.lemmas[i] == "já" or self.lemmas[i] == "můj") and "p1" in self.tags[i]:
                self.new_form = icher_rule_replace_me_forms(self.tags[i], self.member, protg)





