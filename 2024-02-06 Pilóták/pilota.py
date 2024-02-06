class Pilota:
    def __init__(self, sor: str):
        #Lewis Hamilton;1985.01.07;brit;44
        adatok = sor.strip().split(';')
        self.nev = adatok[0]
        self.szuletes = adatok[1]
        self.nemzetiseg = adatok[2]
        
        if adatok[3] == '':
            self.rajtszam = -1
        else:
            self.rajtszam = int(adatok[3])
        
        ev, honap, nap = self.szuletes.split('.')
        self.szuletesi_ev = int(ev)
