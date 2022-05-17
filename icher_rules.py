from Genders import Gender
from Members import Member
from Protagonist import Protagonist
from morph import Morph

from utils import *


# REPLACE PERSONAL PRONOUNS
def icher_rule_replace_me_forms(lemma, tag: str, member: Member, protg: Protagonist, isfirst: bool) -> str:
    gtag = "g" + protg.gender.name
    if decide_use_name():
        case = get_tag_part(tag, "c")
        filtered = list(filter(lambda f: gtag in f[1] and "c" + case in f[1], protg.forms))
        if filtered:
            return filtered[0][0]

    new_tag = tag.replace("xPp1", "p3" + gtag) + "xP"
    new_forms = Morph.get_words("on", new_tag)
    if not new_forms:
        return Morph.get_words(lemma, tag)[0]

    if len(new_forms) > 1:
        if member == Member.prep_object:
            after_prep_forms = list(filter(lambda x: x[0] == "n", new_forms))
            if after_prep_forms:
                return after_prep_forms[0]

    first_forms = list(filter(lambda x: x[0] != "n", new_forms))
    if not first_forms:
        return new_forms[0]

    if gtag != "gF" and isfirst:
        return max(first_forms, key=len)
    return min(first_forms, key=len)


# REPLACE POSSESIVE PRONOUNS
def icher_rule_replace_mine_forms(lemma: str, tag: str, protg: Protagonist) -> str:
    # note: possesives would be replaced by pronouns

    if protg.poss_name and decide_use_names():
        pass

    new_tag = tag.replace("xOp1", "p3") + "xO"
    if lemma == "můj":
        form = "její" if protg.gender == Gender.F else "jeho"
    elif lemma == "náš":
        form = "jejich"

    new_forms = Morph.get_words(form, new_tag)
    if new_forms:
        return new_forms[0]
    return form


# REPLACE VERBS IN PRESENT TENSE AND CONDITIONALS, CONJUNCTIONS
def icher_rule_replace_predicates(word) -> str:
    tag = word.tag

    if "p1" in tag and (("mI" in tag or "mB" in tag) or "mC" in tag):
        tag = tag.replace('p1', 'p3')
        new_forms = generate_new_forms(word.lemma, tag)
        if new_forms:
            return new_forms[0]
    # other cases
    return word.word


# REPLACE or DELETE AUXILIARY VERBS
def icher_rule_replace_delete_auxverb(word) -> str:
    tag = word.tag
    if "p1" not in tag:
        return word.word
    parent_mode = get_tag_part(word.parent_node.tag, "m")
    if "mI" in word.tag:
        if word.parent_node and parent_mode == "A":
            return ''
        elif word.parent_node and patent_mode == "N":
            tag = tag.replace('p1', 'p3')
            new_forms = generate_new_forms(word.lemma, tag)
            if new_forms:
                return new_forms[0]
    return word.word


def generate_new_forms(lemma, tag) -> list:
    new_tag = tag.replace("p1", "p3")
    new_forms = Morph.get_words(lemma, new_tag)
    return new_forms

