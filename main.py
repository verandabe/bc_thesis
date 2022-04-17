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

text = "„Děkujeme za doprovod, Tio,“ říká má společnice.\n “Con piacere,” skloní dívka hlavu a odejde. Vstoupíme do společenské místnosti, která se od zbytku domu značně liší. Zatímco vše, co jsme dosud viděli, bylo v černé a tmavě hnědé, tato místnost je jiná. Zdi jsou v odstínu světle šedé, podlaha je o něco tmavší. Po velké místnosti je roztroušeno několik bílých stolů s tmavými dřevěnými židlemi, jenž sem vůbec nesedí."
rerich = RephrasErIch(Form.ICH)
rerich.create_protagonist("Martin")
print(rerich.rephrase(text))



