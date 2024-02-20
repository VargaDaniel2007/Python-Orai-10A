class Kuldetes:
    def __init__(self, sor: str):
        adatok = sor.strip().split(';')
        self.kod = adatok[0]
        self.datum = adatok[1]
        self.ursiklo = adatok[2]
        self.nap = int(adatok[3])
        self.ora = int(adatok[4])
        self.landolas = adatok[5]
        self.legenyseg = int(adatok[6])

        self.osszes_ora = self.nap * 24 + self.ora