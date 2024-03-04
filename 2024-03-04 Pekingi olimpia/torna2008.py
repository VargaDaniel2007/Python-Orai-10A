from versenyzo import Versenyzo

versenyzok: list[Versenyzo] = []

def main():
    beolvasas()
    print('2. feladat')
    print(f'Összesen {len(versenyzok)} versenyző indult a versenyen')
    korlat_gyoztes()
    rajtszam_kereses()
    kiesett()
    foldreszek()
    orszagok()
    franciak()
    lolenges_europai_atlag()

def beolvasas():
    f = open('torna.csv', 'r', encoding='utf-8')
    f.readline()
    for sor in f:
        versenyzok.append(Versenyzo(sor))
    f.close()

def korlat_gyoztes():
    legjobb: Versenyzo = versenyzok[0]
    for v in versenyzok[1:]:
        if v.korlat > legjobb.korlat:
            legjobb = v
    print('3. feladat')
    print(f'Korlátom {legjobb.nev} szerezte az aranyérmet.')

def rajtszam_kereses():
    print('4. feladat')
    keresett_rajtszam = input('Kérem a versenyző rajtszámát: ')
    i = 0
    while i < len(versenyzok) and versenyzok[i].rajtszam != keresett_rajtszam:
        i += 1
    
    if i < len(versenyzok):
        print(f'A {keresett_rajtszam} rajtszámú versenyző gyűrűn elért eredménye: {versenyzok[i].gyuru}')
    else:
        print('Nincs ilyen versenyző!')

def kiesett():
    print('5. feladat')
    print('Lólengésben nem jutottak dontőbe')
    for v in versenyzok:
        if v.lolenges < 14.5:
            print(f'\t{v.nev}')

def foldreszek():
    print('6. feladat')
    foldreszek = []
    for v in versenyzok:
        if v.foldresz not in foldreszek:
            foldreszek.append(v.foldresz)
    foldreszek.sort()

    print('Földrészek, amelyekről versenyzők indultak:', end=' ')
    for f in foldreszek:
        print(f, end=' ')

def orszagok():
    stat = dict()
    for v in versenyzok:
        if v.orszag in stat.keys():
            stat[v.orszag] += 1
        else:
            stat[v.orszag] = 1
    print('7. feladat')
    for key, value in stat.items():
        if value >= 2:
            print(f'\t{key}: {value} fő')

def franciak():
    f = open('francia.txt', 'w', encoding='utf-8')
    for v in versenyzok:
        if v.orszag == 'FRA':
            f.write(f'{v.rajtszam};{v.nev};{v.osszpontszam()}\n')
    f.close()

def lolenges_europai_atlag():
    print('\n+1. feladat')
    ossz = 0
    db = 0
    for v in versenyzok:
        if v.foldresz == 'Európa':
            ossz += v.lolenges
            db += 1
    print(f'Az európai versenyzők lólengési átlaga: {ossz/db} pont')


main()