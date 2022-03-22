import os

SET_JSON_PATH = "/"
AARA_PATH = "/"
DESAMB_PATH = "/corpora/programy/desamb.utf8.majka.sh"
UNITOK_PATH = "/corpora/programy/unitok.py.czech"
SET_PATH = "/nlp/projekty/set/set/set.py"

class Anaph:

    aara_command = "echo {text} | " + UNITOK_PATH + " | " + DESAMB_PATH\
                   + " | " + SET_PATH + " | " + SET_JSON_PATH + " | " + AARA_PATH

    @classmethod
    def resolve(cls, text: str) -> dict:
        output = os.popen(cls.aara_command.format(options="", text=text))
        aara_output = output.read()
        anaphors: dict = cls.parse_aara_output(aara_output)
        return anaphors

    @classmethod
    def parse_aara_output(cls, aara_output: str) -> dict:
        return {} # TODO
