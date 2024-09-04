class CBadas:

    def __init__(self, sor: str):
        adatok = sor.strip().split(';')

        self.ora = int(adatok[0])
        self.perc = int(adatok[1])
        self.adasdb = int(adatok[2])
        self.nev = adatok[3]
