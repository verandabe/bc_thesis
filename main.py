import sys

sys.path.append('./enums/')
sys.path.append('./classes/')
sys.path.append('./tools/')
sys.path.append('./')
sys.path.append('./eval/')

from RephrasErIch import RephrasErIch
from Forms import Form
from Word import Word
from Protagonist import Protagonist
from Members import Member
from syn import Syn

from eval_data import *

# create_pairs()

text = "Udělal jsem to, abych tě ochránil."
rerich = RephrasErIch(Form.ICH)
rerich.create_protagonist("Martin")
print(rerich.rephrase(text))



