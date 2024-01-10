class Kutya:

    def __init__(self, nev, fajta, eletero = 50):
        self.nev = nev
        self.fajta = fajta
        if eletero > 100 or eletero <= 0:
            raise Exception('Hibás életerő érték')
        self.eletero = eletero    # max 100

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
            