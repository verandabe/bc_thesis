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

#create_pairs()


text = "Petr chce, aby máma plakala."

rerich = RephrasErIch(Form.ER)
rerich.create_protagonist("máma")
print(rerich.rephrase(text))
#'''


