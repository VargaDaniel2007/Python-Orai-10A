from eredmeny import Eredmeny

eredmenyek: list[Eredmeny] = []

def main():
    beolvasas()

    print('3.feladat')
    print(f'Pontszerző helyezések száma: {len(eredmenyek)}')
    erem_statisztika()
    osszpontszam()
    uszas_vs_torna()
    uj_fajl()
    legtobb_sportolo()

def beolvasas():
    f = open('helsinki.txt', 'r')
    for sor in f:
        eredmenyek.append(Eredmeny(sor))
    f.close()

def erem_statisztika():
    arany = 0
    ezust = 0
    bronz = 0
    for e in eredmenyek:
        if e.helyezes == 1:
            arany +=1
        elif e.helyezes == 2:
            ezust +=1
        elif e.helyezes == 3:
            bronz +=1
    '''
        match e.helyezes:
            case 1:
                arany +=1
            case 2:
                ezust +=1
            case 3:
                bronz +=1
    '''            
    print('4. feladat:')
    print(f'Arany: {arany}')
    print(f'Ezüst: {ezust}')
    print(f'Bronz: {bronz}')

def osszpontszam():
    ossz = 0
    for e in eredmenyek:
        ossz += e.pont()

    print('5. feladat')
    print(f'Olimpia pontok száma: {ossz}')

def uszas_vs_torna():
    uszas = 0
    torna = 0
    for e in eredmenyek:
        if e.sportag == 'uszas' and e.helyezes <= 3:
            uszas += 1
        elif e.sportag == 'torna' and e.helyezes <= 3:
            torna += 1

    print('6. feladat:')
    if uszas > torna:
        print('Úszás sportágban szereztek több érmet')
    elif uszas < torna:
        print('Torna sportágban szereztek több érmet')
    else:
        print('Egyenlő volt az érmek száma')

def uj_fajl():
    f = open('helsinki2.txt', 'w')
    for e in eredmenyek:
        f.write(f'{e.helyezes} {e.sportolokSzama} {e.pont()} {e.sportag.replace('kajakkenu', 'kajak-kenu')} {e.versenyszam}\n')

    f.close()

def legtobb_sportolo():
    legtobb: Eredmeny = eredmenyek[0]
    for e in eredmenyek:
        if e.sportolokSzama > legtobb.sportolokSzama:
            legtobb = e
    print('8. feladat: ')
    print(f'Helyezés: {legtobb.helyezes}')
    print(f'Sportág: {legtobb.sportag}')
    print(f'Versenyszám: {legtobb.versenyszam}')
    print(f'Sportolók száma: {legtobb.sportolokSzama}')

main()