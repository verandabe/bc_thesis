import re
from typing import List

# very simplified sentence segmenter, to be updated
def sentence_segment(text: str) -> List[str]:
    sen_seps = '([^.?!]+[.?!]+)'
    return re.findall(sen_seps, text)


def postprocess(rephrased: list):
    return rephrased  # TODO