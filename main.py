import sys
sys.path.append('./enums/')
sys.path.append('./classes/')
sys.path.append('./tools/')
sys.path.append('./')
from syn import Syn

from RephrasErIch import RephrasErIch
from Forms import Form
from Word import Word
from Protagonist import Protagonist
from Members import Member


rerich = RephrasErIch(Form.ICH)

pokus = Word(1, "jsem", 'auxiliary-verb', 2, [], {}, False)
pokus.member = Member.auxiliary_verb
pokus.generate_new_form(Form.ICH, Protagonist("Pavel"))
print(pokus.new_form)
pokus.generate_new_form(Form.ICH, Protagonist("Marie"))
print(pokus.new_form)


