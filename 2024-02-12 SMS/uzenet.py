class Uzenet:
    def __init__(self, sor1: str, sor2: str):
        adatok = sor1.strip().split(' ')
        self.ora = int(adatok[0])
        self.perc = int(adatok[1])
        self.telefonszam = adatok[2]

        self.uzenet = sor2.strip()