from vasarlas import Vasarlas

vasarlasok: list[Vasarlas] = []

def main():
    beolvasas('penztar.txt')
    fizetesek_szama()
    cikkek_szama(1)


def beolvasas(fajl_nev: str):
    f = open(fajl_nev, 'r', encoding='utf-8')
    kovetkezo_vasarlas: Vasarlas = Vasarlas()
    for sor in f:
        sor = sor.strip()
        if sor == 'F':
            vasarlasok.append(kovetkezo_vasarlas)
            kovetkezo_vasarlas = Vasarlas()
        else:
            kovetkezo_vasarlas.hozzaad(sor)

    f.close()

def fizetesek_szama():
    print('2. feladat')
    print(f'A fizetések száma: {len(vasarlasok)}')

def cikkek_szama(vasarlo: int):
    print('\n3. feladat')
    print(f'A(z) {vasarlo}. vásárló {vasarlasok[vasarlo-1].cikkek_szama()} db árucikket vásárolt')

main()