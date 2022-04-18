from Genders import Gender
from morph import Morph
from utils import *


class Protagonist:
    """
    Represents a Protagonist of a text being converted
    """

    def __init__(self, name: str, poss_name=None):
        self.name = name
        self.poss_name = poss_name
        self.forms = self._try_generate_forms(poss=False)
        self.gender = self._get_gender()
        self.forms_own_loaded = False

    def _try_generate_forms(self, poss=False):
        """
        Tries to generate forms of the protagonist's name if majka can decline it.
        Otherwise, returns calling of load_own_forms method.
        """
        generated = Morph.get_wt(self.name)

        if generated:
            return list(filter(lambda f: "nS" in f[1], generated))

        self.forms_own_loaded = True

        load_or_create = "g"
        while load_or_create not in "CL":
            load_or_create = input("Forms not generated.\nFor adding forms manually, press C.\nFor loading forms from a file, press L.")
        if load_or_create == "C":
            return self._create_forms()

        filename = input("Enter name of the file with forms: ")
        return load_own_forms(self, filename)


    def load_own_forms(self, file_name=None):
        """
        Loads the forms of protagonist's name from a given file in form "lemma tag\n"
        If file_name not given, returns calling of _create_forms method.
        """
        # nacti rucne vysklonovane jmeno, kdyz majka nezvladne
        # file ve formatu: ```lemma tag\n```

        if file_name is None:
            return self._create_forms()

        forms = []
        with open(file_name, "r") as df:
            declist = df.read().split('\n')

        for form in declist:
            forms.append(tuple(form.split()))

        return forms

    def _create_forms(self):
        """
        Loads protagonist name's forms and tags as user input.
        """

        print("Creating forms for Protagonist, ", self.name)
        gender = "g"
        while gender not in "fFmMnN":
            gender = input("Protagonist's gender (F/M/N):  ").upper()

        declined_forms = []

        tag = "k1g{gender}nSc{case}"
        for i in range(1, 8):
            word_form = input("Form in {case}. case:  ".format(case=i))
            declined_forms.append((word_form, tag.format(gender=gender, case=i)))

        return declined_forms

    def _get_gender(self):
        for form in self.forms:
            tag = form[1]
            g = get_tag_part(tag, "g")
            return Gender(g)
        return Gender.MASC  # default gender i guess








