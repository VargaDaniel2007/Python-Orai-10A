class Felfedez:
    def __init__(self, sor: str):
        data = sor.strip().split(';')
        if data[0] == 'Ókor':
            self.ev = -1
        else:
            self.ev = int(data[0])
        self.nev = data[1]
        self.vegyj = data[2]
        self.rends = int(data[3])
        self.felf = data[4]