from morph import Morph
from Genders import Gender

class Protagonist:
    """
    Represents a Protagonist of a text being converted
    """

    def __init__(self, name: str):
        self.name = name
        self.forms = self._try_generate_forms()
        self.gender = self._get_gender()

    def _try_generate_forms(self):
        """
        Tries to generate forms of the protagonist's name if majka can decline it.
        Otherwise, returns calling of load_own_forms method.
        """
        generated = Morph.get_wt(self.name)
        if generated:
            return generated

        return self.load_own_forms()

    def load_own_forms(self, file_name=None): # TODO
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
            for letter_index in range(0, len(tag), 2):
                if tag[letter_index] == "g":
                    return Gender(tag[letter_index+1])
        return Gender.MASC  # default gender i guess








