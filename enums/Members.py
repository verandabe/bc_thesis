from enum import Enum

class Member(Enum):

    # super members
    sentence = '<sentence>'
    clause = '<clause>'
    coord = '<coord>'

    # not as described members
    verb = 'verb'
    other = 'other'

    # as described members
    auxiliary_verb = 'auxiliary-verb'
    subject = 'subject'
    subject_bad = 'subject-bad'
    object = 'object'
    verb_object = 'verb-object'
    modifier = 'modifier'
    adverb = 'adverb'
    additional_prep = 'additional-prep'
    prep_object = 'prep-object'

