from morph import Morph

class Word:
    """
    Class representing a word.
    """

    def __init__(self, index, string: str, member, parent_idx, dependents, anaphor, ds: bool):
        self.index = index
        self.word = string
        self.lemma = Morph.get_lemma(string) # TODO
        self.tag = Morph.get_tag(string)
        self.member = member
        self.parent_idx = parent_idx
        self.dependents = dependents
        self.new_form = string+"_new"
        self.anaphor = anaphor
        self.direct_speech = ds

    def generate_new_form(self) -> str:  # TODO
        return self.word

    def is_real_word(self) -> bool:
        return "<" not in self.word

