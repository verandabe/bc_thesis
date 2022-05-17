from Forms import Form
from Members import Member
from icher_rules import *
from erich_rules import *

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
        self.member = member
        self.parent_idx = parent_idx
        self.parent_node = None
        self.dependents = dependents
        self.new_form = string
        self.anaphor = anaphor
        self.direct_speech = ds
        self.unex_subject = None  # Only for predicates

    def generate_new_form(self, form: Form, protg: Protagonist) -> None:
        if self.direct_speech:
            self.process_direct_speech()

        elif form == Form.ICH:
            self._ich_to_er(protg)

        elif form == Form.ER:
            self._er_to_ich(protg)

    def is_real_word(self) -> bool:
        return "<" not in self.word

    def _ich_to_er(self, protg: Protagonist) -> None:
        if self.member == Member.pred or self.member == Member.y:
            self.new_form = icher_rule_replace_predicates(self)
        elif self.member == Member.auxiliary_verb:
            if "kY" in self.tag:
                self.new_form = icher_rule_replace_predicates(self)
            else:
                self.new_form = icher_rule_replace_delete_auxverb(self)
        else:
            if ((self.lemma == "já" or self.anaphor == "já") or (self.lemma == "my")) and "p1" in self.tag:
                first = self.index == 0
                self.new_form = icher_rule_replace_me_forms(self.lemma, self.tag, self.member, protg, first)
            elif (self.lemma == "můj" or self.lemma == "náš") and "p1" in self.tag:
                self.new_form = icher_rule_replace_mine_forms(self.lemma, self.tag, protg)

    def _er_to_ich(self, protg: Protagonist) -> None:
        if self.lemma == protg.name or not self.lemma or self.anaphor == protg.name:
            self.new_form = erich_rule_replace_name(self, protg)
        if self.member == Member.pred:
            if "p3" in self.tag:
                self.new_form = erich_rule_replace_pred(self, protg)
            else:
                result_tuple = erich_rule_add_auxverb(self, protg)
                if not result_tuple[1]:
                    self.new_form = result_tuple[0]
                elif find_local_subject(self):
                    self.new_form = result_tuple[1] + " " + result_tuple[0]
                else:
                    self.new_form = result_tuple[0] + " " + result_tuple[1]
        elif self.member == Member.auxiliary_verb and "p3" in self.tag:
            self.new_form = erich_rule_replace_auxverb(self, protg)
        elif "k3" in self.tag and "xP" in self.tag and "p3" in self.tag:
            self.new_form = erich_rule_replace_personal_pronouns(self, protg)

    def process_direct_speech(self) -> None:
        self.new_form = self.word.replace('_', ' ')
