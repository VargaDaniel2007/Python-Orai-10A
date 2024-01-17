from dij import Nobel

dijak: list[Nobel] = []

def main():
    beolvasas()
    valasz = nevKereses('Arthur B.','McDonald')
    print(f'3. feladat: {valasz}')
    valasz = evTipusKereses('irodalmi',2017)
    print(f'4. feladat: {valasz.keresztn} {valasz.vezetekn}')
    bekeDij()
    curie()
    dijSzam()
    orvosi()
    


def beolvasas():
    f = open('nobel.csv', 'r', encoding='utf-8')
    f.readline()
    for sor in f:
        item = Nobel(sor)
        dijak.append(item)
    
    f.close()

def nevKereses(kersztnev: str, vezeteknev: str) -> Nobel:
    i = 0
    while len(dijak) > i and dijak[i].keresztn != kersztnev and dijak[i].vezetekn != vezeteknev:
        i +=1
    return dijak[i].tipus

def evTipusKereses(tipusa: str, eve: int) -> str:
    i = 0
    while len(dijak) > i and dijak[i].tipus != 'irodalmi' or dijak[i].ev != 2017:
        i += 1
    return dijak[i]

def bekeDij():
    print('5. feladat:')
    for dij in dijak:
        if dij.ev >= 1990 and dij.vezetekn == '' and dij.tipus == 'béke':
            print(f'\t{dij.ev}: {dij.keresztn}')

def curie():
    print('6. feladat:')
    for dij in dijak:
        if 'Curie' in dij.vezetekn:
            print(f'\t{dij.ev}: {dij.keresztn} {dij.vezetekn}')
        
def dijSzam():
    bekeDB = 0
    irodalmiDB = 0
    fizikaiDB = 0
    orvosiDB = 0
    kemiaiDB = 0
    kozgazdDB = 0
    for dij in dijak:
        if dij.tipus == 'béke':
            bekeDB += 1
        elif dij.tipus == 'irodalmi':
            irodalmiDB += 1
        elif dij.tipus == 'fizikai':
            fizikaiDB += 1
        elif dij.tipus == 'orvosi':
            orvosiDB += 1
        elif dij.tipus == 'kémiai':
            kemiaiDB += 1
        elif dij.tipus == 'közgazdaságtani':
            kozgazdDB += 1
    print('7. feladat:')
    print(f'\tfizikai\t\t\t{fizikaiDB} db')
    print(f'\tkémiai\t\t\t{kemiaiDB} db')
    print(f'\torvosi\t\t\t{orvosiDB} db')
    print(f'\tirodalmi\t\t{irodalmiDB} db')
    print(f'\tbéke\t\t\t{bekeDB} db')
    print(f'\tközgazdaságtani\t\t {kozgazdDB} db')

def orvosi():
    orvosidijak: list[Nobel] = []
    f = open('orvosi.txt', 'w', encoding='utf-8')
    for dij in dijak:
        if dij.tipus == 'orvosi':
            orvosidijak.append(dij)
    orvosidijak.reverse()
    for orvosi in orvosidijak:
        f.write(f'{orvosi.ev}:{orvosi.keresztn} {orvosi.vezetekn}\n')
    f.close()

main()