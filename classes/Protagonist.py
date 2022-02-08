#from tools.morph import Morph

class Protagonist:

    def __init__(self, name: str):
        self.name = name
        self.forms = _try_generate_forms()
        self.gender = None # TODO


    def _try_generate_forms(self):
        #generated = Morph.get_wt(name)
        generated = None
        if bool(generated):
            return generated

        return self.load_own_forms()


    def load_own_forms(self): # TODO
        # nacti rucne vysklonovane jmeno, kdyz majka nezvladne
        pass

