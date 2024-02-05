class Fizetes:
    def __init__(self, sor:str):
        #Név;Fizetés
        #Sipos Lajos;505000
        adatok = sor.strip().split(';')
        self.nev = adatok[0]
        self.fizetes = int(adatok[1])
        