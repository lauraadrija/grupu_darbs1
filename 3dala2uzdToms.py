#2. uzdevums

class Skolotajs:
    def __init__(self, uzvards, stundu_skaits, tips):
        self.uzvards = uzvards
        self.stundu_skaits = stundu_skaits
        self.tips = tips


class SakumskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, klase, stundu_skaits):
        super().__init__(uzvards, stundu_skaits, 1)
        self.klase = klase

    def izdrukat(self):
        print(f"Sākumskolas (tips – {self.tips}) skolotājs {self.uzvards} māca "
              f"{self.stundu_skaits} stundas {self.klase} klasē.")


class VidusskolasSkolotajs(Skolotajs):
    def __init__(self, uzvards, prieksmets1, stundas1, prieksmets2, stundas2):
        super().__init__(uzvards, 0, 3)
        self.prieksmets1 = prieksmets1
        self.prieksmets2 = prieksmets2
        self.stundas1 = stundas1
        self.stundas2 = stundas2
        self.stundu_kopskaits = self.aprekinat_kopskaitu()

    def aprekinat_kopskaitu(self):
        return self.stundas1 + self.stundas2

    def izdrukat(self):
        print(f"Vidusskolas (tips – {self.tips}) skolotājs {self.uzvards} māca "
              f"šādus priekšmetus: {self.prieksmets1} un {self.prieksmets2}, "
              f"kopā {self.stundu_kopskaits} stundas.")


# Datu ievade
uzvards_sak = input("Ievadiet sākumskolas skolotāja uzvārdu: ")
klase = input("Ievadiet skolotāja klasi: ")
stundas_sak = int(input("Ievadiet skolotāja stundu skaitu: "))

uzvards_vid = input("Ievadiet vidusskolas skolotāja uzvārdu: ")
prieksmets1 = input("Ievadiet pirmo pasniegto priekšmetu: ")
stundas1 = int(input("Ievadiet pirmā priekšmeta stundu skaitu: "))
prieksmets2 = input("Ievadiet otro pasniegto priekšmetu: ")
stundas2 = int(input("Ievadiet otrā priekšmeta stundu skaitu: "))

# Objektu izveide
sakumskolas_skolotajs = SakumskolasSkolotajs(uzvards_sak, klase, stundas_sak)
vidusskolas_skolotajs = VidusskolasSkolotajs(
    uzvards_vid, prieksmets1, stundas1, prieksmets2, stundas2)
