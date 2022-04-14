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

create_pairs()

'''
text = "V dospívání jsem dávala najevo vzdor, ale nikdy jsem to nevzala radikálně. Matka i Maryska mě vedly k dospělosti velmi přísně. Záviděla jsem holkám v parku, jak se smějí, objímají se svými chlapci, líbají se. „Vidíš ty holky?“ zeptala se jednou matka, když si všimla, že hledím z okna a pozoruji je. „Starej se jen o sebe a jdi za tím, po čem toužíš. Úspěch. Jsi jen ty, tvrdá cesta a úspěch. Muž tě jen odradí, ublíží ti a přivede tě k neúspěchu. Rozumíš?“ Chtěla jsem něco namítnout, ale mlčky jsem přikývla."

rerich = RephrasErIch(Form.ICH)
rerich.create_protagonist("Stella")
print(rerich.rephrase(text))

text = "Tom a David nikdy nepochopili, proč je Anička nemá ráda. „Tom je prostě často smutný,“ vysvětlil mu to jednou Pavel. Tom na to nereagoval. \n On neví, co si Anicka myslí."
text1 = "Tomáš nevěděl, ale máma mu poradila."
rerich = RephrasErIch(Form.ER)
rerich.create_protagonist("Tomáš")
print(rerich.rephrase(text1))
'''


