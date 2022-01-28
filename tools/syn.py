import os
from typing import List

from tools.morph import Morph

SET_PATH = "../set/"

class Syn:

    command = SET_PATH + "set.py {options} {filename}"

    @staticmethod
    def _generate_vertical(sentence: str) -> str:
        words = sentence.split() # TODO tokenize sentence

        with open("tmp/sentence_input.txt", "w") as f:
            for word in words:
                f.write(word)
                f.write('\t')
                lts = Morph.get_lt(word)
                for tup in lts:
                    f.write(tup[0] + ',')
                f.write('\t')
                for tup in lts:
                    f.write(tup[1] + ',')
                f.write('\n')

            filename = f.name

        return filename

    @classmethod
    def get_sentence_nodes(cls, sentence: str) -> List[List[str]]:
        vertical_input_filename = cls._generate_vertical(sentence)
        output = os.popen(cls.command.format(options="", filename=vertical_input_filename))
        sentence = output.read()
        nodes = [ node.split('\t') for node in sentence.split('\n') ][:-1]
        return nodes

