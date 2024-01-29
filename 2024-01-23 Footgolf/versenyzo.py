class Versenyzo:

    def __init__(self, sor: str) -> None:
        # Albert Laszlo;Felnott ferfi;HOLE HUNTERS;0;0;10;10;0;0;0;10
        adatok = sor.strip().split(';')
        self.nev = adatok[0]
        self.kategoria = adatok[1]
        self.egyesulet = adatok[2]
        
        self.pontok: list[int] = []
        for p in adatok[3:]:
            self.pontok.append(int(p))
        
    def osszpontszam(self)
        pontszam = 0

        temp = []
        for p in self.pontok:
            temp.append(p)

        for i in range(2):
            min = temp[0]
            for p in temp:
                if p < min:
                    min = p

            if min > 0:
                pontszam += 10        
            temp.remove(min)

        for p in temp:
            pontszam += p

        return pontszam
        
        
