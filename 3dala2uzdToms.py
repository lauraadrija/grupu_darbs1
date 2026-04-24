#2. uzdevums

class Skolotajs:
    def __init__(self, uzvards, stundu_skaits, tips):
        self.uzvards = uzvards
        self.stundu_skaits = stundu_skaits
        self.tips = tips

class Sakumskolotjas:
    def __init__(self, uzvards, klase, stundu_skaits):
        super().__init__(uzvards, stundu_skaits, 1)
        self.klase = klase
    
    def izdrukat(self):
        print(f"Sākumskolas (tips - {self.tips}) skolotājs {self.uzvards} māca " f"{self.stundu_skaits} stundas {self.klase} klasē. ")