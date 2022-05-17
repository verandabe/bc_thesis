import sys

sys.path.append('./enums/')
sys.path.append('./classes/')
sys.path.append('./tools/')
sys.path.append('./')

from RephrasErIch import RephrasErIch
from Forms import Form


text = "Pověsil jsem kabát na dřevěný věšák u vchodu, očima vyhledal modré křeslo ve tvaru kapky a sedl si na stoličku naproti němu. Rozhlédl jsem se po kavárně. U okna seděla docela sympatická dívka s chlapcem, drželi se za ruce. V rohu pod policí knih posedávala postarší žena -- myslím, že jí mohlo být tak sedmdesát -- začtená do jednoho z výtisků. A nakonec světlovlasá baristka silnější postavy a tvářemi tak rudými, jako by to byla ona, kdo právě unikl náruči prosincové noci. Trochu mi připomínala učitelku ze školky. S nápojovým lístkem v rukou přistoupila ke mně, beze slova mi ho podala a zase se vrátila na své místo za pultem, kde se s nezaujatým výrazem věnovala svému mobilu. Bylo mi jasné, že se nemůže dočkat, až jí skončí směna."

rerich = RephrasErIch(Form.ICH)
rerich.create_protagonist("Matyáš")
print(rerich.rephrase(text))


