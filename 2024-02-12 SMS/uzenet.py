class Uzenet:
    def __init__(self, sor1: str, sor2: str):
        adatok = sor1.strip().split(' ')
        self.ora = int(adatok[0])
        self.perc = int(adatok[1])
        self.telefonszam = adatok[2]

        self.uzenet = sor2.strip()

    def uzenet_hossz_kategoria(self) -> str:    #1-20, 21-40 ...
        if len(self.uzenet) > 80:
            return '81-100'
        if len(self.uzenet) > 60:
            return '61-80'
        if len(self.uzenet) > 40:
            return '41-60'
        if len(self.uzenet) > 20:
            return '21-40'
        return '1-20'