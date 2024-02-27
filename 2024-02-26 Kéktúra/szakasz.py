class Szakasz:
    def __init__ (self, sor:str):
        adatok = sor.strip().split(';')
        self.honnan = adatok[0]
        self.hova = adatok[1]
        self.tavolsag = float(adatok[2].replace(',','.'))
        self.fel = int(adatok[3])
        self.le = int(adatok[4])
        self.pecsetelohely = (adatok[5] == 'i')


    def HianyosNev(self) -> bool:
        if not self.pecsetelohely:
            return False
        '''
        if 'pecsetelohely' in self.hova:
            return False
        return True
        '''
        return 'pecsetelohely' not in self. hova