class Hegycsucs:

    def __init__ (self,sor):
        # Ágasvár;Mátra;789
        adatok = sor.strip().split(';')     # ['Ágasvár', 'Mátra', '789']
        self.nev = adatok[0]
        self.hegyseg = adatok[1]
        self.magassag = int(adatok[2])

        