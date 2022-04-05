from Forms import Form
from Members import Member
from icher_rules import *
from erich_rules import *
from morph import Morph

from Protagonist import Protagonist


class Word:
    """
    Class representing a word.
    """

    def __init__(self, index, string: str, member: Member, parent_idx, dependents, anaphor: str, ds: bool):
        self.index = index
        self.word = string
        self.lemma = None
        self.tag = None
        # self.lts = Morph.get_lt(string)
        self.member = member
        self.parent_idx = parent_idx
        self.parent_node = None
        self.dependents = dependents
        self.new_form = string#+"_new"  # TODO delete after testing
        self.anaphor = anaphor
        self.direct_speech = ds
        self.unex_subject = None  # Only for predicates

    def generate_new_form(self, form: Form, protg: Protagonist):  # TODO
        if not self.is_real_word() or self.direct_speech:
            return

        if form == Form.ICH:
            self.ich_to_er(protg)

        elif form == Form.ER:
            self.er_to_ich(protg)

    def is_real_word(self) -> bool:
        return "<" not in self.word

    def ich_to_er(self, protg: Protagonist):
        if self.member == Member.pred:
            self.new_form = icher_rule_replace_predicates(self)
        elif self.member == Member.auxiliary_verb or self.member == Member.y:
            self.new_form = icher_rule_replace_delete_auxverb(self)
        else:
            if (self.lemma == "já" or self.anaphor == "já") and "p1" in self.tag:
                first = self.index == 0  # TODO
                self.new_form = icher_rule_replace_me_forms(self.tag, self.member, protg, first)
            elif (self.lemma == "můj" or self.anaphor == "já") and "p1" in self.tag:
                self.new_form = icher_rule_replace_mine_forms(self.tag, protg)

    def er_to_ich(self, protg: Protagonist):
        if self.lemma == protg.name or not self.lemma:
            self.new_form = erich_rule_replace_name(self, protg)
        if self.member == Member.pred:
            if "p3" in self.tag:
                self.new_form = erich_rule_replace_pred(self, protg)
            else:
                result_tuple = erich_rule_add_auxverb(self, protg)
                if not result_tuple[1]:
                    self.new_form = result_tuple[0]
                elif find_local_subject(self):  # TODO some pravidlo ah idk
                    self.new_form = result_tuple[1] + " " + result_tuple[0]
                else:
                    self.new_form = result_tuple[0] + " " + result_tuple[1]
        elif self.member == Member.auxiliary_verb and "p3" in self.tag:
            self.new_form = erich_rule_replace_auxverb(self, protg)
        elif "k3" in self.tag and "xP" in self.tag and "p3" in self.tag:
            self.new_form = erich_rule_replace_personal_pronouns(self, protg)

