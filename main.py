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

text = "Je mi příšerná zima, mám obrovský strach a třesu se jako osika. Ležím na zádech v blátě a lehký letní déšť mi padá na obličej a do oka. Studí… Velmi mě bolí nohy, jako by mi je někdo drtil ve svěráku. Nemohu se nadechnout, ačkoliv bych chtěl. Tak rád bych se ještě aspoň jednou nadechl… Srdce mi přestane bít, ačkoliv se s tou kulkou v sobě vážně snažilo. Pohled se mi zamlžuje, ale i tak vidím, jak nade mnou stojí neznámá žena s puškou v ruce. Její obličej nerozeznám, ale slyším, že pláče. Z posledních sil otočím hlavu. Bahno kolem mě se zbarvuje do ruda. Vím, že mojí krví. Chtěl bych řvát bolestí, nebo plakat, ale na to sílu už nemám. Sleduji třicet párů bot mužů stojících kolem mě."

rerich = RephrasErIch(Form.ICH)


rerich.create_protagonist("Adam")
print(rerich.rephrase(text))

