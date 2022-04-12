import os
import re

SET_JSON_PATH = "../set_json.py"
AARA_PATH = "../aara5.py"
DESAMB_PATH = "/corpora/programy/desamb.utf8.majka.sh"
UNITOK_PATH = "/corpora/programy/unitok.py.czech"
SET_PATH = "/nlp/projekty/set/set/set.py --marx"

class Anaph:

    aara_command = "echo {text} | " + UNITOK_PATH + " | " + DESAMB_PATH + " | " + SET_PATH + " | " + SET_JSON_PATH + " | " + AARA_PATH

    @classmethod
    def resolve(cls, text: str) -> dict:
        output = os.popen(cls.aara_command.format(text=text))
        aara_output = output.read()
        anaphors: dict = cls.parse_aara_output(aara_output)
        print(anaphors)
        return anaphors

    @classmethod
    def parse_aara_output(cls, aara_output: str) -> dict:
        aara_output = aara_output.replace("\n", "")
        sentences = re.findall(r'(<s>.+?(?=<\/s>))', aara_output)
        anaph_dict = {}
        for sentence in sentences:
            old = re.search(r'(<o>.+?(?=<\/o>))', sentence).group(0)[3:]
            diffs = re.findall(r'(<d>.*?(?=<\/d>))', sentence)
            non_empty_diffs = list(filter(lambda d: len(d) > 3, diffs))
            diffs = [tuple(diff[3:].split('-')) for diff in non_empty_diffs]
            anaph_dict[old] = dict(diffs)
        print("tools/anaph:  anaph_dict:  ", anaph_dict)
        return anaph_dict
