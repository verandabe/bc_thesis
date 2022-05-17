import re
from typing import List
from random import random

PROTG_NAME_USAGE_PROBABILITY = 0.2

# very simplified sentence segmenter, to be updated
def sentence_segment(text: str) -> List[str]:
    sen_seps = '([^\s][^.?!]*[.?!]+)'
    return re.findall(sen_seps, text)


def get_tag_part(tag: str, category: str) -> str:
    for letter_idx in range(0, len(tag), 2):
        if tag[letter_idx] == category:
            return tag[letter_idx + 1]


def postprocess(rephrased) -> List[str]:
    postprocessed = []
    for p in range(len(rephrased)):
        ds_postpo = re.sub('_', ' ', rephrased[p])
        diac_postpo = re.sub('([„\[\({])(\s)', r'\1', ds_postpo)
        diac_postpo = re.sub('(\s)([,;:?!.}\)\]“])', r'\2', diac_postpo)
        postprocessed.append(diac_postpo)
    return postprocessed


def decide_use_name(prob=None) -> bool:
    rand = random()
    return rand < (PROTG_NAME_USAGE_PROBABILITY if prob is None else prob)

