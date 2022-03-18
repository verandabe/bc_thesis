import sys

sys.path.append('./enums/')
sys.path.append('./classes/')
sys.path.append('./tools/')
sys.path.append('./')

from RephrasErIch import RephrasErIch
from Forms import Form
from Word import Word
from Protagonist import Protagonist
from Members import Member



rerich = RephrasErIch(Form.ICH)


rerich.create_protagonist("Petr")
print(rerich.rephrase("Chci vidět maminku, ale není tu. Včera jsem pracoval na zahradě a teď mě z toho bolí záda."))



