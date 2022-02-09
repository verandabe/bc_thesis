from Text import Text
from Protagonist import Protagonist
from Forms import Form

class RephrasErIch:

    def __init__(self, from_form: Form, protg: Protagonist = None):
        self.form = from_form
        self.protg = protg
        self.text = None


    def rephrase(self, text: str):
        self.text = Text(text, self.form)

        if self.form == Form.ICH:
            self._ich_to_er()
        else:
            if self.protg is None:
                print("Missing protagonist")
                return
            self._er_to_ich()


    def set_form(self, from_form: Form):
        self.form = from_form


    def create_protagonist(self, name: str, gender = None):
        self.protg = Protagonist(name) # TODO when classes ready


    def _ich_to_er(self):
        pass


    def _er_to_ich(self):
        pass


rerich = RephrasErIch(Form.ICH)
rerich.rephrase("Jsem princezna")
