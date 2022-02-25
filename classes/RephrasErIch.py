from Text import Text
from Protagonist import Protagonist
from Forms import Form
from utils import postprocess

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

        if self.form == Form.ER and self.protg is None:
            print("Missing protagonist. Create protagonist first.")
            return

        self.text = Text(text, self.form, self.protg)

        rephrased_list = []
        for p in self.text.paragraphs:
            rephrased_par = []
            for s in p.sentences:
                s.rephrase(self.form)
                for w in s.words:
                    if w.is_real_word():
                        rephrased_par.append(w.new_form)
            rephrased_list.append(" ".join(rephrased_par))

        rephrased_list = postprocess(rephrased_list)
        rephrased_text = "\n".join(rephrased_list)
        return rephrased_text

    def set_form(self, from_form: Form):
        self.form = from_form

    def create_protagonist(self, name: str):
        self.protg = Protagonist(name)

