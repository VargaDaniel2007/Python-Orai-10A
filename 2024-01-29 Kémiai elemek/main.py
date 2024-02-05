from felfed import Felfedez

felfedezes: list[Felfedez] = []

def main():
    betoltes()
    print(f'3. feladat: Elemek száma: {len(felfedezes)}')
    okor()
    kereses(bekeres())
    leghosszabb()
    #Megoldás 2 / 7. feladat:
    elozoEv = -1
    max = -1
    for e in felfedezes:
        if elozoEv != -1 and elozoEv != -1:
            if max < e.ev - elozoEv:
                max = e.ev - elozoEv
        elozoEv = e.ev

    print(f'7. feladat: {max}')

def betoltes():
    f = open('felfedezesek.csv', 'r', encoding='utf-8')

    f.readline()
    for sor in f:
        felfedezes.append(Felfedez(sor))
    f.close()

def okor():
    db = 0
    for elem in felfedezes:
        if elem.ev == -1:
            db += 1
    print(f'4. feladat: Felfedezések száma az ókorban: {db}')

def bekeres() -> str:
    vegyjel = ''
    while len(vegyjel) == 0 or len(vegyjel) > 2 or vegyjel.lower()[0] < 'a' or vegyjel.lower()[0] > 'z' or (len(vegyjel) == 2 and vegyjel.lower() < 'a') or (len(vegyjel) == 2 and vegyjel.lower() > 'z'):
        vegyjel = input('5. feladat: Kérek egy vegyjelet: ')
    return vegyjel

def kereses(vegyjel: str):
    i = 0
    while i < len(felfedezes) and felfedezes[i].vegyj.lower() != vegyjel.lower():
        i += 1
    print(f'6. feladat: Keresés')
    if i < len(felfedezes):
        print(f'\tAz elem vegyjele: {felfedezes[i].vegyj}\n'
              f'\tAz elem neve: {felfedezes[i].nev}\n'
              f'\tRendszáma: {felfedezes[i].rends}\n'
              f'\tFelfedezés éve: {felfedezes[i].ev}\n'
              f'\tFelfedező: {felfedezes[i].felf}')
    else:
        print('\tNincs ilyen elem az adatforrásban!')

def leghosszabb():
    maxEv = 0
    for i in range(1, len(felfedezes)-1):
        if felfedezes[i].ev != -1:
            if felfedezes[i+1].ev-felfedezes[i].ev > maxEv:
                maxEv = felfedezes[i+1].ev-felfedezes[i].ev
            

    print(f'7. feladat: {maxEv} év volt a leghosszabb időszak két elem felfedezése között.')





main()