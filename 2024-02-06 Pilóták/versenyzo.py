from pilota import Pilota

versenyzok: list[Pilota] = []

def main():
    beolvasas()
    print(f'3. feladat: {len(versenyzok)}')
    print(f'4. feladat: {versenyzok[-1].nev}')
    szazad19()
    legkisebb_rajtszam()    


def beolvasas():
    f = open('pilotak.csv', 'r', encoding='utf-8')
    f.readline()
    for sor in f:
        versenyzok.append(Pilota(sor))
    f.close()

def szazad19():
    print('5. feladat:')
    for v in versenyzok:
        if v.szuletesi_ev < 1901:
            print(f'\t{v.nev} ({v.szuletes})')

def legkisebb_rajtszam():
    legkisebb: Pilota = None
    for v in versenyzok:
        if v.rajtszam >= 0 and (legkisebb == None or v.rajtszam < legkisebb.rajtszam):
            legkisebb = v
    print(f'6. feladat: {legkisebb.nemzetiseg}')


main()