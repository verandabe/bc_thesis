from typing import List, Dict

from Forms import Form
from Members import Member
from syn import Syn
from morph import Morph

from Protagonist import Protagonist
from Word import Word
from icher_rules import *
from erich_rules import *

class Sentence:
    """
    Class object representing a sentence
    """

    def __init__(self, sentence: str, anaphors: Dict[str, str], protg):
        self.nodes = Syn.get_sentence_nodes(sentence)
        self.anaphors = anaphors
        self.words = self._create_words_objects()
        self.root = self._find_root()
        self.protg = protg
        self._add_parents()
        self.new_sentence = sentence

    def _create_words_objects(self) -> List[Word]:
        """
        Method creates a list of Word objects from nodes generated by SET.
        """
        words = []
        ds = False
        for node in self.nodes:
            index, word_form, parent_idx, _, member, _, wlt = node
            anaphor = None
            #if word_form.lower() in self.anaphors:
            #    anaphor = self.anaphors[word_form.lower()]
            anaphor = None
            word = Word(int(index),
                        word_form,
                        member,
                        int(parent_idx),
                        [],
                        anaphor,
                        ds)
            if wlt:
                word.lemma = wlt[1]
                word.tag = wlt[2]
            word.member = self._assign_member(word)
            if word.lemma in self.anaphors:
                word.anaphor = self.anaphors[word.lemma]
            words.append(word)

            if word_form == "„": ds = True
            elif word_form == "“": ds = False

        self._add_dependencies(words)
        self._add_unexpressed_subject(words)

        return words

    def _add_dependencies(self, words: List[Word]) -> None:
        """
        Takes the undone list of Word objects and updates it by adding dependending Word objects to dependencies.
        """
        for i, node in enumerate(self.nodes):
            dep_idx = int(node[2])
            words[dep_idx].dependents.append(words[i])

    def _add_parents(self) -> None:
        for word in self.words:
            if word.parent_idx == -1:
                continue
            word.parent_node = self.words[word.parent_idx]

    def _add_unexpressed_subject(self, words: List[Word]):
        if "_" not in self.anaphors:
            return
        for word in words:
            if word.member == Member.pred:
                if find_local_subject(word):
                    return
                word.unex_subject = self.anaphors["_"]


    def _find_root(self) -> Word:
        """
        Method takes the Word objects list and finds the root of sentence tree.
        """
        for word in self.words:
            if word.parent_idx == -1:
                return word

    def _is_word_predicate(self, word: Word) -> bool:
        if len(word.member) > 0:
            return False
        tag = word.tag
        return tag and len(tag) > 1 and tag[1] == "5"

    def _is_word_cond(self, word: Word) -> bool:
        if len(word.member) > 0:
            return False
        lemma = word.lemma
        return lemma == "kdyby" or lemma == "aby"

    def _assign_member(self, word: Word) -> Member:
        if self._is_word_predicate(word):
            return Member.pred
        if self._is_word_cond(word):
            return Member.y
        if Member.has_value(word.member):
            return Member(word.member)
        return Member.other

    def rephrase(self, form: Form):
        new_forms = []
        first = True
        names_considered = True
        for word in self.words:
            if not word.is_real_word():
                continue
            word.generate_new_form(form, self.protg)

        for word in self.words:
            if not word.is_real_word():
                continue
            if first and word.new_form:
                first = False
                word.new_form = word.new_form[0].upper() + word.new_form[1:]

            if names_considered and form == Form.ICH:
                no_consider = self._deal_with_names(word, new_forms, first)
                if no_consider:
                    names_considered = False
            else:
                new_forms.append(word.new_form)

        self.new_sentence = " ".join(new_forms)

    def _deal_with_names(self, word, new_forms, first) -> bool:
        add_name_index = self._name_should_be_added(word)

        if add_name_index == -1:
            new_forms.append(self.protg.name)
        new_forms.append(word.new_form)
        if add_name_index == 1:
            new_forms.append(self.protg.name)

        return add_name_index

    def _name_should_be_added(self, word: Word) -> int:
        if not decide_use_name() or not word.tag:
            return 0

        in_front = "k5" in word.tag
        if in_front or "kY" in word.tag:
            if word.word != word.new_form:
                if self.protg.name not in [word_str for word_str in self.words]:
                    return -1 if in_front else 1
        return 0

