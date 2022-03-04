import sys
sys.path.append('./enums/')
sys.path.append('./classes/')
sys.path.append('./tools/')
sys.path.append('./')


from RephrasErIch import RephrasErIch
from Forms import Form
from Word import Word
from Protagonist import Protagonist

rerich = RephrasErIch(Form.ICH)

pokus = Word(1, "mnou", "s", 2, [], {}, False)
pokus.generate_new_form(Form.ICH, Protagonist("Pavel"))
print(pokus.new_form)