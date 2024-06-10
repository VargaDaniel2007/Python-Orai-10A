class Fogadasi_fordulo:
     def __init__(self, sor: str):
          adatok = sor.strip().split(';')

          self.ev = int(adatok[0])
          self.het = int(adatok[1])
          self.fordulo = int(adatok[2])
          self.t13p1 = int(adatok[3])
          self.ny13p1 = int(adatok[4])
          self.eredmenyek = adatok[5]