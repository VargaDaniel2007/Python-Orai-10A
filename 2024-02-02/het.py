class Het:
    def __init__(self, sor: str):
        adatok = sor.split(' ')
        self.szamok: list[int] = []
        for a in adatok:
            self.szamok.append(int(a))