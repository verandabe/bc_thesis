from morph import Morph
from Protagonist import Protagonist
from Word import Word


def erich_rule_replace_name(word: Word, protg: Protagonist):
    for form in protg.forms:
        if form == word.word:
            case = get_tag_part(word.tag, "c")
            new_tag = "k3p1nSc" + str(case) + "xP"
            new_forms = Morph.get_words("já", new_tag)
            if new_forms:
                return new_forms[-1]
    return word.word

def erich_rule_replace_pred():
    pass


def erich_rule_replace_auxverb():
    pass


def erich_rule_add_auxverb():
    pass


def erich_rule_replace_personal_pronouns():
    pass


def erich_rule_replace_possessive_pronouns():
    pass
