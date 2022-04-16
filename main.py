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

text = "Zpěv ustal a kazatel se pustil do čtení dalšího úryvku z Bible. Pak přišla její oblíbená část – kázání. Marie se posadila, vytáhla deník a zapisovala si nápady, které ji zaujaly. Kazatel byl velmi dobrý řečník, jeho projev v jejím sešitu snad pokaždé něco zanechal.\n„Jenže vždycky záleží, jak své vlastnosti využijeme. On svou sebejistotu využil špatným způsobem. Ona totiž moc člověka změní – ale málokdy k lepšímu.”\nU té myšlenky se propiska zarazila v půlce věty a Marie se podívala na kazatele. A pak se podruhé pokusila soustředit.\nTehdy si Marie uvědomila, že hlavní důvod, proč do kostela dál chodí, je pocit, že ji někdo drží, že úplně všechno bude v pořádku."
rerich = RephrasErIch(Form.ER)
rerich.create_protagonist("Marie")
print(rerich.rephrase(text))



