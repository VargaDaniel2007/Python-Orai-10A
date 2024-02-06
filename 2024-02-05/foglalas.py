class Foglalas:
    def __init__(self, sor: str):
        #Csorba Ede 16:30 2017.10.28-18:48
        adatok = sor.strip().split(' ')
        self.nev = f'{adatok[0]} {adatok[1]}'
        self.idopont = adatok[2]
        self.foglalas_idopont = adatok[3]

        oopp = self.idopont.split(':')      #['16', '30']
        self.percek = int(oopp[0]) * 60 + int(oopp[1])
