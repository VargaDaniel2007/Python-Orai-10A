from varos import Varos

varosok: list[Varos] = []

def main():
    beolvasas()

    print(f'3. feladat: A listában {len(varosok)} város szerepel.')

    print(f'4. feladat: Legalább 10 milliós városok száma: {tobb_mint_10_millio()}.')

    legnepesebb = legnepesebb_varos()
    print(f'5. feladat: Legnépesebb város:')
    print(f'\tNeve: {legnepesebb.nev}')
    print(f'\tOrszág: {legnepesebb.orszag}')
    print(f'\tLakosság: {legnepesebb.lakossag}')

    kinaiak = kinai_lakosok()
    print(f'A {kinaiak[0]}, legnagyobb kínai város összlakossága {kinaiak[1]}')
def beolvasas():
    f = open('varosok.csv', 'r', encoding='utf-8')
    f.readline()
    for sor in f:
        varosok.append(Varos(sor))
    f.close()

def tobb_mint_10_millio() -> int:
    db = 0
    for v in varosok:
        if v.lakossag > 10000000:
            db +=1
    return db

def legnepesebb_varos() -> Varos:
    max = varosok[0]
    for v in varosok:
        if v.lakossag > max.lakossag:
            max = v
        
    return max

def kinai_lakosok() -> []:      #első elem: db, második elem: lakosság
    db = 0 
    osszlakossag = 0
    for v in varosok:
        if v.orszag == 'Kína':
            db += 1
            osszlakossag += v.lakossag

    return [db, osszlakossag]

main()