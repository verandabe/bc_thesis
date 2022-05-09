import sys

sys.path.append('./enums/')
sys.path.append('./classes/')
sys.path.append('./tools/')
sys.path.append('./')

from RephrasErIch import RephrasErIch
from Forms import Form


text = "Petr chce, aby máma plakala."

rerich = RephrasErIch(Form.ER)
rerich.create_protagonist("máma")
print(rerich.rephrase(text))


