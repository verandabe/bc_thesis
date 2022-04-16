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

text = "Nikdy jsem si nemyslela, že by se mi něco takového mohlo stát. Máma lpěla na mém vzdělání a já netušila, jak jí vysvětlit, že mě to nezajímá. Táta často mluvil o mých známkách, ale k mému zklamání toho nikdy nenechal."
rerich = RephrasErIch(Form.ICH)
rerich.create_protagonist("Stella")
print(rerich.rephrase(text))



