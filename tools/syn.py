import os
from typing import List, Tuple

# SET_PATH = "../set/" home
SET_PATH = "/nlp/projekty/set/set/set.py"
DESAMB_PATH = "/corpora/programy/desamb.utf8.majka.sh"
UNITOK_PATH = "/corpora/programy/unitok.py.czech"


class Syn:
    """
    Class providing the usage of SET, syntactic analyzer.
    """

    command = "echo {sentence} | " + UNITOK_PATH + " | " + DESAMB_PATH + " | " + SET_PATH
    des_command = "echo {sentence} | " + UNITOK_PATH + " | " + DESAMB_PATH

    @classmethod
    def get_sentence_nodes(cls, sentence: str) -> List[List[str]]:
        """
        Transforms a sentence to a tree generated by SET.
        :param sentence: string, sentence to be analyzed
        :return: list of words with metadata in form [index, word, dependency index, dep/phr, member type]
        """
        # vertical_input_filename = cls._generate_vertical(sentence)
        # output = os.popen(cls.command.format(options="", filename=vertical_input_filename))
        output = os.popen(cls.des_command.format(options="", sentence=sentence))
        desamb_output = output.read()
        morph_info: List[Tuple[str]] = cls._get_morph_info_from_sen(desamb_output)
        set_output = os.popen(cls.command.format(options="", sentence=sentence)).read()
        nodes = [node.split('\t') for node in set_output.split('\n')][:-1]
        cls._add_morph_info(morph_info, nodes)
        return nodes

    @classmethod
    def _get_morph_info_from_sen(cls, desamb_output: str):
        wlts = []
        for line in desamb_output.split("\n"):
            if line and line[0] != "<":
                wlt = tuple(line.split("\t")) # word, lemma, tag
                wlts.append(wlt)
        return wlts

    @classmethod
    def _add_morph_info(cls, morph_infos: List[Tuple[str]], nodes: list):
        t = 0
        for n in range(len(nodes)):
            if t > len(morph_infos) - 1:
                nodes[n].append(None)
            else:
                if morph_infos[t][0] == nodes[n][1]:
                    nodes[n].append(morph_infos[t])
                    t += 1

