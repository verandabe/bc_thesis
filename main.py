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
from syn import Syn

text = "Tom a David nikdy nepochopili, proč je Anička nemá ráda. „Tom je prostě často smutný,“ vysvětlil mu to jednou Pavel. Tom na to nereagoval. \n On neví, co si Anicka myslí."
text1 = "Tomáš nevěděl, ale máma mu poradila."
rerich = RephrasErIch(Form.ER)
rerich.create_protagonist("Tomáš")
print(rerich.rephrase(text1))
