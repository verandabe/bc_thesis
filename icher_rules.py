from morph import Morph
from Members import Member
from Protagonist import Protagonist

def icher_rule_replace_me_forms(tag: str, member: Member, protg: Protagonist):
    gtag = "g" + protg.gender.name
    new_tag = tag.replace("p1", "p3" + gtag)
    new_forms = Morph.get_words("on", new_tag)

    if member == Member.prep_object:
        return new_forms[1]
    return new_forms[0]


def icher_rule_replace_mine_forms():
    pass
