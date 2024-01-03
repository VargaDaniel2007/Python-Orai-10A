class Kutya:

    def __init__(self, nev, fajta):
        self.nev = nev
        self.fajta = fajta
        self.eletero = 50           #max 100

    def allapot(self) -> str:
        if self.eletero < 20:
            return 'éhes'
        if self.eletero < 40:
            return 'fáradt'
        if self.eletero < 80:
            return 'normál'
        return 'életvidám'
    
    def eszik(self):
        if self.eletero > 80:
            raise Exception('Az eb nem elég éhes')
        else:
            self.eletero += 20

    def mozog(self):
        if self.eletero < 20:
            raise Exception('Az eb inkább enne')
        else:
            self.eletero -= 10
