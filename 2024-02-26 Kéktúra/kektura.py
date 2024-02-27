from szakasz import Szakasz

szakaszok: list[Szakasz] = []

def main():
    indulo_magassag = beolvasas()
    print(f'3. feladat: Szakaszok száma: {len(szakaszok)} db')
    tura_hossza()
    legrovidebb_szakasz()
    hianyos_allomasnevek()
    legmagasabb_vegpont(indulo_magassag)
    javitott_allomany(indulo_magassag)

def beolvasas() -> int:
    f = open('kektura.csv', 'r', encoding='utf-8')
    m = int(f.readline().strip())
    for sor in f:
        szakaszok.append(Szakasz(sor))

    f.close()
    return m

def tura_hossza():
    ossz = 0
    for sz in szakaszok:
        ossz += sz.tavolsag
    print(f'4. feladat: A túra teljes hossza: {ossz:.3f} km')

def legrovidebb_szakasz():
    min: Szakasz = szakaszok[0]
    for sz in szakaszok[1:]:
        if sz.tavolsag < min.tavolsag:
            min = sz
    print('5. feladat: A legrövidebb szakasz adatai:')
    print(f'\tKezdete: {min.honnan}')
    print(f'\tVége: {min.hova}')
    print(f'\tTávolság: {min.tavolsag} km')

def hianyos_allomasnevek():
    print('7. feladat: Hiányos állomásnevek:')
    db = 0
    for sz in szakaszok:
        if sz.HianyosNev():
            print(f'\t{sz.hova}')
            db += 1
    if db == 0:
        print('\tNincs hiányos állomásnév')

def legmagasabb_vegpont(magassag):
    legmagasabb = szakaszok[0]
    magassag += (szakaszok[0].fel - szakaszok[0].le)
    maxMagassag = magassag
    for sz in szakaszok[1:]:
        magassag += (sz.fel - sz.le)
        if magassag > maxMagassag:
            legmagasabb = sz
            maxMagassag = magassag

    print('8. feladat: A túra legmagasabban fekvő végpontja:')
    print(f'\tVégpont neve: {legmagasabb.hova}')
    print(f'\tTegerszint feletti magassága: {maxMagassag} m')
            
def javitott_allomany(indulo_magassag):
    f = open('kektura2.csv', 'w', encoding='utf-8')
    f.write(f'{indulo_magassag}\n')
    for sz in szakaszok:
        hova = sz.hova
        if sz.HianyosNev():
            hova += " pecsetelohely"

        pecset = 'n'
        if sz.pecsetelohely:
            pecset = 'i'
        f.write('{0};{1};{2};{3};{4};{5}\n'.format(
            sz.honnan,
            hova,
            sz.tavolsag,
            sz.fel,
            sz.le,
            pecset
        ))
    f.close()
main()