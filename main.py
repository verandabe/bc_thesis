import sys
sys.path.append('./enums/')
sys.path.append('./classes/')
sys.path.append('./tools/')

'''
from RephrasErIch import RephrasErIch
from Forms import Form

rerich = RephrasErIch(Form.ER)
rerich.rephrase("lalala")
'''

from Protagonist import Protagonist
protg = Protagonist("Helena")
print(protg.name)
print(protg.forms)

protg = Protagonist("Meda")
print(protg.name)
print(protg.forms)

