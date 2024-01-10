class Varos:

    def __init__(self, sor: str):
        adatok = sor.strip().split(';')         #['Bangkok','Thaiföld','5696409']
        self.nev = adatok[0]
        self.orszag = adatok[1]
        self.lakossag = int(adatok[2])
