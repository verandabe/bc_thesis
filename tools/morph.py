import os
from typing import List, Tuple

MAJKA_PATH = '../majka/'
MAJKA_DATA_PATH = '../majka/data/'


class Morph:

    command = 'echo "{word}" | ' + MAJKA_PATH + 'majk -f ' + MAJKA_DATA_PATH + '{data_file}'


    @classmethod
    def _get_tuples(cls, word: str, data_file: str) -> List[Tuple[str]]:
        cmd = cls.command.format(word=word, data_file=data_file)
        output = os.popen(cmd)
        tmp = output.read().replace('\n', ':').split(':')
        tuples = []

        for i in range(0, len(tmp)-1, 2):
            tuples.append((tmp[i], tmp[i+1]))

        return tuples


    @classmethod
    def get_lt(cls, word: str) -> List[Tuple[str]]:
        return cls._get_tuples(word, "majka.w-lt")


    @classmethod
    def get_wt(cls, lemma: str) -> List[Tuple[str]]:
        return cls._get_tuples(lemma, "majka.l-wt")


    @classmethod
    def get_lemma(cls, word: str) -> str:
        lts = cls.get_lt(word)
        if bool(lts):
            lemma, _ = lts[0]
            return lemma
        return word


    @classmethod
    def get_tag(cls, word: str) -> str:
        lts = cls.get_lt(word)
        if bool(lts):
            _, tag = lts[0]
            return tag


    @classmethod
    def get_word(cls, lemma: str, tag: str) -> List[str]:
        cmd = cls.command.format(word=lemma+':'+tag, data_file="majka.lt-w")
        output = os.popen(cmd)
        words = output.read().split('\n')
        return words[:-1]

