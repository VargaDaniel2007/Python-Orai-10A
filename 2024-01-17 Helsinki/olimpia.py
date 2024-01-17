class Helyezes:
    def __init__(self, sor: str):
        data = sor.strip().split(' ')
        self.helyezes = int(data[0])
        self.sportolok = int(data[1])
        self.sportag = data[2]
        self.versenysz = data[3]