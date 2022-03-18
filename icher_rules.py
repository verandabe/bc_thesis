from random import random

from Genders import Gender
from Members import Member
from Protagonist import Protagonist
from morph import Morph

from utils import *

PROTG_NAME_USAGE_PROBABILITY = 0.5


# REPLACE PERSONAL PRONOUNS
def icher_rule_replace_me_forms(tag: str, member: Member, protg: Protagonist):
    gtag = "g" + protg.gender.name
    if decide_use_name():
        case = get_tag_part(tag, "c")
        filtered = list(filter(lambda f: gtag in f[1] and "c" + case in f[1], protg.forms))
        if filtered:
            return filtered[0][0]

    new_tag = tag.replace("p1", "p3" + gtag)
    new_forms = Morph.get_words("on", new_tag)

    if member == Member.prep_object:
        return new_forms[1]
    return new_forms[0]


# REPLACE POSSESIVE PRONOUNS
def icher_rule_replace_mine_forms(tag: str, protg: Protagonist): # TODO opravit
    # new_tag = tag.replace("xOp1", "p3") + "xO"  # kdyz vertical generuje set (taguje ajka)
    new_tag = tag.replace("p1", "p3")
    form = "její" if protg.gender == Gender.F else "jeho"
    # TODO načítání i přivlastnovaci tvary jmena? zatim nahrazovat zajmenem
    new_form = Morph.get_words(form, new_tag)[0]
    return new_form


# REPLACE VERBS IN PRESENT TENSE AND CONDITIONAL
def icher_rule_replace_predicates(word):
    tag = word.tag
    if "p1" in tag and ("mI" in tag or "mB" in tag):
        new_tag = tag.replace("p1", "p3")
        new_form = Morph.get_words(word.lemma, new_tag)[0]  # todo?
        return new_form
    # other cases
    return word.word


# REPLACE or DELETE AUXILIARY VERBS
def icher_rule_replace_delete_auxverb(word):
    tag = word.tag
    if tag and "k5" in tag:
        if "p1" not in tag:
            return word.word
        if word.parent_node and word.parent_node.member == Member.pred:
            return ''
    new_tag = tag.replace("p1", "p3")
    new_form = Morph.get_words(word.lemma, new_tag)[0]  # todo?
    return new_form


def decide_use_name(prob=None) -> bool:
    rand = random()
    return rand < (PROTG_NAME_USAGE_PROBABILITY if prob is None else prob)
