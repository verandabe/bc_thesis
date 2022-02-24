from Text import Text
from Protagonist import Protagonist
from Forms import Form

class RephrasErIch:
    """
    Class representing the tool converting texts with given protagonist from given form.
    """
    def __init__(self, from_form: Form, protg: Protagonist = None):
        self.form = from_form
        self.protg = protg
        self.text = None

    def rephrase(self, text: str) -> str:
        """
        Rephrase a given text from its form to the other form.
        :param text: text to be converted
        :return: rephrased text
        """
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

    def create_protagonist(self, name: str):
        self.protg = Protagonist(name)

    def _ich_to_er(self):
        """
        Convert the text from first person to third person.
        """
        pass

    def _er_to_ich(self):
        """
        Convert the text from third person to first person.
        """
        pass


rerich = RephrasErIch(Form.ICH)
rerich.rephrase("Jsem princezna")
