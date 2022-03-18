import os
from typing import List

from tools.morph import Morph

# SET_PATH = "../set/" home
SET_PATH = "/nlp/projekty/set/set/set.py"
DESAMB_PATH = "/corpora/programy/desamb.utf8.majka.sh"
UNITOK_PATH = "/corpora/programy/unitok.py.czech"


class Syn:
    """
    Class providing the usage of SET, syntactic analyzer.
    """

    # command = SET_PATH + "set.py {options} {filename}"
    command = "echo {sentence} | " + UNITOK_PATH + " | " + DESAMB_PATH + " | " + SET_PATH


    '''
    @staticmethod
    def _generate_vertical(sentence: str) -> str:
        """
        Generate a vertical file for given sentence to be used as SET input.
        :param sentence: string, sentence to transform to vertical data
        :return: name of a file where the vertical data is written
        """

        words = sentence.split()  # TODO sentence segmention

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
    
    '''

    @classmethod
    def get_sentence_nodes(cls, sentence: str) -> List[List[str]]:
        """
        Transforms a sentence to a tree generated by SET.
        :param sentence: string, sentence to be analyzed
        :return: list of words with metadata in form [index, word, dependency index, dep/phr, member type]
        """
        # vertical_input_filename = cls._generate_vertical(sentence)  # TODO generate by SET
        # output = os.popen(cls.command.format(options="", filename=vertical_input_filename))
        output = os.popen(cls.command.format(options="", sentence=sentence))
        sentence = output.read()
        nodes: List[List[str]] = [node.split('\t') for node in sentence.split('\n')][:-1]
        return nodes

