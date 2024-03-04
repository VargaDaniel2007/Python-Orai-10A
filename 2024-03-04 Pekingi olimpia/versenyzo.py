class Versenyzo:
    def __init__(self, sor: str):
        adatok = sor.strip().split(';')

        self.rajtszam = adatok[0]
        self.nev = adatok[1]
        self.orszag = adatok[2]
        self.foldresz = adatok[3]
        self.talaj = float(adatok[4].replace(',','.'))
        self.lolenges = float(adatok[5].replace(',','.'))
        self.gyuru = float(adatok[6].replace(',','.'))
        self.nyujto = float(adatok[7].replace(',','.'))
        self.korlat = float(adatok[8].replace(',','.'))
        self.ugras = float(adatok[9].replace(',','.'))

    def osszpontszam(self):
        return self.talaj + self.lolenges + self.gyuru + self.nyujto + self.korlat + self.ugras
        
