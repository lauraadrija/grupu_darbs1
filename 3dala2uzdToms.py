#2. uzdevums

class Skolotajs:
    def __init__(self, uzvards, stundu_skaits, tips):
        self.uzvards = uzvards
        self.stundu_skaits = stundu_skaits
        self.tips = tips

class SakumskolasSkolotajas:
    def __init__(self, uzvards, klase, stundu_skaits):
        super().__init__(uzvards, stundu_skaits, 1)
        self.klase = klase
    
    def izdrukat(self):
        print(f"Sākumskolas (tips - {self.tips}) skolotājs {self.uzvards} māca " f"{self.stundu_skaits} stundas {self.klase} klasē. ")

class VidusskolasSkolotajas (Skolotajs):
    def __init__(self, uzvards, prieksmets1 , stundas1, prieksmets2, stundas2):
        super().__init__(uzvards, 0, 3)
        self.prieksmets1 = prieksmets1
        self.prieksmets2 = prieksmets2
        self.stundas1 = stundas1
        self.stundas2 = stundas2
        self.stundu_kopskaits = self.stundu_kopskaits()

    def aprekinat_kopskaitu(self):
        return self.stundas1 + self.stundas2
    
    def izdrukat(self):
        print(f"vidusskolas (tips - {self.tips}) skolotājs {self.uzvards} māca"
              f"Šādus priekšmetus: {self.prieksmets1} un {self.prieksmets2},"
              f"kopā {self.stundu_kopskaits} stundas.")
        
# Datu ievade
uzvards_sak = input("Ievadiet sākumskolas skolotāja uzvārdu: ")
klase = input("Ievadiet skolotāja klasi:")
stundas_sak = int(input("Ievadiet skolotāja stundu skaitu: "))

uzvards_vid = input("Ievadiet vidusskolas skolotāja uzvārdu: ")
prieksmets1 = input("Ievadiet pirmo pasniegto")
