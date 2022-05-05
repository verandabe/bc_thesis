from morph import Morph
from Protagonist import Protagonist
from Members import Member

from utils import *


# REPLACE NAMES
def erich_rule_replace_name(word, protg: Protagonist):
    for form in protg.forms:
        case = get_tag_part(word.tag, "c")
        if form[0] == word.word or form[0] == word.anaphor:
            skip_name = not decide_use_name(0.4) and case == '1'
            if skip_name and word.parent_node.word != "<coord>":
                return ""

            new_tag = "k3p1nSc" + str(case) + "xP"
            new_forms = Morph.get_words("já", new_tag)

            if new_forms:
                return new_forms[-1]
    return word.word


# REPLACE PREDICATES
def erich_rule_replace_pred(word, protg: Protagonist):
    tag = word.tag
    if "p3" in tag and ("mI" in tag or "mB" in tag):
        subject = find_local_subject(word)
        if (subject and (subject.lemma == protg.name or subject.anaphor == protg.name))\
            or word.unex_subject == protg.name:
            new_tag = tag.replace("p3", "p1")
            new_forms = Morph.get_words(word.lemma, new_tag)
            if new_forms:
                return new_forms[0]  # todo?
    return word.word


# REPLACE CONDITIONAL FORMS
def erich_rule_replace_auxverb(word, protg: Protagonist):
    # word.member == Member.auxiliary_verb and "p3" in word.tag:
    pred_ancestor = find_pred_ancestor(word)
    subject = find_local_subject(pred_ancestor)
    if subject:
        if (subject.lemma == protg.name or subject.anaphor == protg.name):
            tag = word.tag
            new_tag = tag.replace("p3", "p1")
            new_forms = Morph.get_words(word.lemma, new_tag)
            if new_forms:
                return new_forms[0]
    return word.word


# ADD AUXILIARY VERBS
def erich_rule_add_auxverb(word, protg: Protagonist) -> tuple:
    # word.member == member.pred and "p" not in tag
    if "mA" in word.tag or "mN" in word.tag:
        subject = find_local_subject(word)
        if (subject and subject.word == "<coord>"):
            subject = protg_in_coord(subject, protg)
        if (subject and (subject.lemma == protg.name
            or subject.anaphor == protg.name)) \
            or word.unex_subject == protg.name:
                number = get_tag_part(word.tag, "n")
                aux_verb_form = "jsem" if number == "S" else "jsme"
                if not erich_rule_replace_conjs(word):
                    return (word.word, aux_verb_form)
    return (word.word, None)
    # kam?


# REPLACE PERSONAL PRONOUNS
def erich_rule_replace_personal_pronouns(word, protg: Protagonist):
    # "xp" and "k3" in word.tag and "p3" in word.tag:
    if protg.name == word.anaphor:
        tag = word.tag
        new_tag = tag.replace("xPp3gM", "p1") + "xP"
        new_forms = Morph.get_words("já", new_tag)
        if new_forms:
            return new_forms[0]
    return word.word


# REPLACE CONJUNCTIONS
def erich_rule_replace_conjs(word) -> bool:
    clause = find_clause_ancestor(word)
    for dep in clause.dependents:
        if dep.lemma == "aby" or dep.lemma == "kdyby":
            new_tag = dep.tag.replace("p3", "p1")
            new_forms = Morph.get_words(dep.lemma, new_tag)
            dep.new_form = new_forms[0]
            return True
    return False


# REPLACE POSSESSIVE PRONOUNS
def erich_rule_replace_possessive_pronouns():
    # not possible with aara :{
    pass


def find_pred_ancestor(word):
    current_ancestor = word.parent_node
    if current_ancestor.member == Member.pred or current_ancestor.member == Member.clause:
        return current_ancestor
    return find_pred_ancestor(current_ancestor)


def find_clause_ancestor(word):
    current_ancestor = word.parent_node
    if current_ancestor.word == "<clause>":
        return current_ancestor
    return find_clause_ancestor(current_ancestor)


def find_local_subject(root):
    for offspring in root.dependents:
        if is_subject(offspring):
            return offspring
        potential_subject = find_local_subject(offspring)
        if potential_subject:
            return potential_subject
    return None


def is_subject(word):
    return word.member == Member.subject or word.member == Member.subject_bad


def protg_in_coord(coord, protg):
    for dep in coord.dependents:
        if dep.word == protg.name:
            return dep
    return coord


