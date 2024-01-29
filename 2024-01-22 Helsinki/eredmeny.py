class Eredmeny:
    
    def __init__(self, sor: str):
        # 1 1 atletika kalapacsvetes
        adatok = sor.strip().split(' ')
        self.helyezes = int(adatok[0])
        self.sportolokSzama = int(adatok[1])
        self.sportag = adatok[2]
        self.versenyszam = adatok[3]

    def pont(self):
        if self.helyezes == 1:
            return 7
        return 7 - self.helyezes

