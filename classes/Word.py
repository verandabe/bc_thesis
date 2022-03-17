from Forms import Form
from Members import Member
from icher_rules import *
from morph import Morph

from Protagonist import Protagonist


class Word:
    """
    Class representing a word.
    """

    def __init__(self, index, string: str, member: Member, parent_idx, dependents, anaphor, ds: bool):
        self.index = index
        self.word = string
        self.lemma = Morph.get_lemma(string)  # TODO
        self.tag = Morph.get_tag(string)
        # self.lts = Morph.get_lt(string)
        self.member = member
        self.parent_idx = parent_idx
        self.parent_node = None
        self.dependents = dependents
        self.new_form = string#+"_new"  # TODO delete after testing
        self.anaphor = anaphor
        self.direct_speech = ds

    def generate_new_form(self, form: Form, protg: Protagonist):  # TODO
        if not self.is_real_word() or self.direct_speech:
            return

        if form == Form.ICH:
            self.ich_to_er(protg)

        elif form == Form.ER:
            pass

    def is_real_word(self) -> bool:
        return "<" not in self.word

    def ich_to_er(self, protg: Protagonist):
        if self.member == Member.pred:
            self.new_form = icher_rule_replace_predicates(self)
        elif self.member == Member.auxiliary_verb or self.member == Member.y:
            self.new_form = icher_rule_replace_delete_auxverb(self)
        else:
            if self.lemma == "já" and "p1" in self.tag:
                self.new_form = icher_rule_replace_me_forms(self.tag, self.member, protg)
            elif self.lemma == "můj" and "p1" in self.tag:
                self.new_form = icher_rule_replace_mine_forms(self.tag, protg)






