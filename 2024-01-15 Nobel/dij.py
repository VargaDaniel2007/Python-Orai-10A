class Nobel:

    def __init__(self, sor: str):
        data = sor.strip().split(';')  #Lista[]
        self.ev = int(data[0])
        self.tipus = data[1]
        self.keresztn = data[2]
        self.vezetekn = data[3]
