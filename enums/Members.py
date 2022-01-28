from enum import Enum

class Member(Enum):
    sentence = '<sentence>'
    clause = '<clause>'

    verb = 0

    auxiliary_verb = 'auxiliary-verb'
    subject = 'subject'
    object = 'object'
    verb_object = 'verb-object'
    modifier = 'modifier'
    adverb = 'adverb'

