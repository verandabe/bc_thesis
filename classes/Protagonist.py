from morph import Morph

class Protagonist:

    def __init__(self, name: str):
        self.name = name
        self.forms = _try_generate_forms()


    def _try_generate_forms(self):
        generated = Morph.get_wt(name)
        :x



            return generated

        return self.load_own_forms()


    def load_own_forms(self, file_name=None): # TODO
        # nacti rucne vysklonovane jmeno, kdyz majka nezvladne
        # file ve formatu: ```lemma tag\n```

        if file_name is None:
            return self._create_forms():

        forms = []
        with open(file_name, "r") as df:
            declist = df.read().split('\n')

        for form in declist:
            forms.append(tuple(form.split()))

        return forms


    def _create_forms(self):
        gender = None
        while gender not in "fFmMnN":
            gender = upper(input("Protagonist's gender: (F/M/N)"))

        declined_forms = []
        tag = "k1g{gender}nSc{case}"
        for i in range(1, 8):
            word_form = input("Form in {case}. case".format(case=i)
            declined_forms.append((word_form, tag.format(gender=gender, case=i)))

        return declined_forms








