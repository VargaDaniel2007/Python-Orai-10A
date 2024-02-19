class Vasarlas:

    def __init__(self):
        self.arucikkek = dict()


    def hozzaad(self, termek: str):
        if termek in self.arucikkek.keys():
            self.arucikkek[termek] += 1
        else:
            self.arucikkek[termek] = 1

    def cikkek_szama(self):
        db = 0
        for value in self.arucikkek.values():
            db += value
        return db
    
    def fizetendo_osszeg(self):
        osszeg = 0
        for value in self.arucikkek.values():
            match value:
                case 1:
                    osszeg += 500
                case 2:
                    osszeg += 950
                case _:                 #Minden más esetben
                    osszeg += 950 + (value-2) * 400
        return osszeg
