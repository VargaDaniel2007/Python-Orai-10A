from vasarlas import Vasarlas

vasarlasok: list[Vasarlas] = []

def main():
    beolvasas('penztar.txt')
    fizetesek_szama()
    cikkek_szama(1)
    arucikk_adatok()
    darabszam()
    vasarlas_adatai()
    bevetel()

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

def arucikk_adatok():
    print('\n5. fekadat')
    arucikk = input('Kérem az árucikk nevét: ')
    elso_index = -1
    utolso_index = -1
    alkalom = 0
    for i in range(0, len(vasarlasok)):
        if arucikk in vasarlasok[i].arucikkek.keys():
            if elso_index == -1:
                elso_index = i
            utolso_index = i
            alkalom += 1
    
    if alkalom == 0:
        print('Ebből a termékből nem vásároltak.')
    else:
        print(f'Az első vásárlás sorszáma: {elso_index+1}')
        print(f'Az utolsó vásárlás sorszáma: {utolso_index+1}')
        print(f'{alkalom} vásárlás során vettek belőle.')

def darabszam():
    print('\n6. feladat')
    db = int(input('Adja meg a vásárolt darabszámot: '))
    print(f'{db} darab vételekor fizetendő: {ertek(db)} Ft')

def ertek(value: int) -> int:
    match value:
        case 1:
            return 500
        case 2:
            return 950
    return 950 + (value-2) * 400

def vasarlas_adatai():
    print('\n7. feladat')
    sorszam = 0
    while sorszam  < 1 or sorszam > len(vasarlasok):
        sorszam = int(input('Adja meg a vásárlás sorszámát: '))

    for key, value in vasarlasok[sorszam-1].arucikkek.items():
        print(f'{value} {key}')

def bevetel():
    f = open('osszeg.txt', 'w', encoding='utf-8')
    for  i in range(0, len(vasarlasok)):
        f.write(f'{i+1}: {vasarlasok[i].fizetendo_osszeg()}\n')

    f.close()

main()