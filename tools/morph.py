import os
from typing import List, Tuple

MAJKA_PATH = '../majka/'
MAJKA_DATA_PATH = '../majka/data/'


class Morph:
    """
        Class providing the usage of Majka, morphological analyzer.
    """

    command = 'echo "{word}" | ' + MAJKA_PATH + 'majk -f ' + MAJKA_DATA_PATH + '{data_file}'

    @classmethod
    def _get_tuples(cls, word: str, data_file: str) -> List[Tuple[str, str]]:
        """
        Generates list of tuples (word, tag) for a given word and dataset.
        """
        cmd = cls.command.format(word=word, data_file=data_file)
        output = os.popen(cmd)
        tmp = output.read().replace('\n', ':').split(':')
        tuples = []

        for i in range(0, len(tmp)-1, 2):
            tuples.append((tmp[i], tmp[i+1]))

        return tuples

    @classmethod
    def get_lt(cls, word: str) -> List[Tuple[str, str]]:
        """
        Generates lemmas and tags for a given word.
        """
        return cls._get_tuples(word, "majka.w-lt")

    @classmethod
    def get_wt(cls, lemma: str) -> List[Tuple[str, str]]:
        """
        Generates all word forms and tags for a given lemma.
        """
        return cls._get_tuples(lemma, "majka.l-wt")

    @classmethod
    def get_lemma(cls, word: str) -> str:
        # TODO vracet vsechny?
        lts = cls.get_lt(word)
        if not lts:
            return word
        lemma, _ = lts[0]
        return lemma

    @classmethod
    def get_lemmas(cls, word: str) -> List[str]:  # alternativa kdyby se vracely vsechny
        lts = cls.get_lt(word)
        if not lts:
            return [word]
        lemmas = [lt[0] for lt in lts]
        return lemmas

    @classmethod
    def get_tag(cls, word: str) -> str:
        lts = cls.get_lt(word)
        if bool(lts):
            _, tag = lts[0]
            return tag

    @classmethod
    def get_tags(cls, word: str):  # podobna alternativa pro tagy
        lts = cls.get_lt(word)
        if not lts:
            return
        tags = [lt[1] for lt in lts]
        return tags

    @classmethod
    def get_words(cls, lemma: str, tag: str) -> List[str]:
        """
        Generates a word forms according to given lemma and tag.
        """
        cmd = cls.command.format(word=lemma+':'+tag, data_file="majka.lt-w")
        output = os.popen(cmd)
        words = output.read().split('\n')
        return words[:-1]

