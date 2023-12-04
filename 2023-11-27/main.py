import os

pontszamok = [54,74,16,52,24,81,88,25,5,18,37,6,0,19,13,95,14,99,66,58,83,19,70,89,59,93,59,41,27,57,4,77,8]

#Feladatok
#   Menü:
#       - Pontszámok átlaga
#       - Kérdezzünk a felhasználótól egy osztályzatot -> írjuk ki hány olyan annak megfelelő doga lett
#           0-20: (1), 21-40: (2), 41-60: (3), 61-80: (4), 81-100: (5)
#       - Legjobb dolgozat -> pontszám és sorszám is
#       - Kérdezzünk a gelhasználótól egy pontszámot -> van-e ilyen pontszámú dolgozat
#       - Keressük meg az első nulla pontos dolgozat sorszámát
#           - Ha nincs, akkor írjuk ki, hogy nincs ilyen

def main():
    m = ''
    while m != '0': 
        m = menu()
        match m:
            case '1':
                atlag()
            case '2':
                osztalyzatDarab2()
            case '3':
                legjobbDolgozat2()
            case '4':
                eldontes2()
            case '5':
                nullaPontos()

def menu() -> str:
    os.system('cls')
    print('1...Pontszámok átlaga')
    print('2...Adott osztályzatok száma')
    print('3...Legjobb dolgozat')
    print('4...Van-e "n" pontszámú dolgozat')
    print('5...Nulla pontos dolgozat keresése')
    print('\n0...Kilépés')

    v = ''
    while v not in ['0', '1', '2', '3', '4', '5']:
        v = input('\nVálasztás: ')
    return v

def atlag():
    os.system('cls')
    ossz = 0
    for pont in pontszamok:
        ossz += pont
    atlag = ossz / len(pontszamok)
    print(f'A pontszámok átlaga: {atlag:.2f}')
    input('\n<Enter>')

def osztalyzatDarab():
    os.system('cls')
    osztalyzat = input('Hányas osztályzatú dolgozatok számára kíváncsi? ')
    min = -1
    max = -1
    match osztalyzat:
        case '1':
            min = 0
            max = 20
        case '2':
            min = 21
            max = 40
        case '3':
            min = 41
            max = 60
        case '4':
            min = 61
            max = 80
        case '5':
            min = 81
            max = 100

    db = 0
    for pont in pontszamok:
        if pont >= min and pont <= max:
            db += 1
    print(f'{osztalyzat}-s osztályzatú dolgozatból {db} db született.')
    input('\n<Enter>')
    
def osztalyzatDarab2():
    os.system('cls')
    osztalyzat = int(input('Hányas osztályzatú dolgozatok számára kíváncsi? '))
    max = osztalyzat * 20
    min = max - 19
    if osztalyzat == 1:
        min = 0
    
    db = 0
    for pont in pontszamok:
        if pont >= min and pont <= max:
            db += 1
    print(f'{osztalyzat}-s osztályzatú dolgozatból {db} db született.')
    input('\n<Enter>')

def legjobbDolgozat():
    os.system('cls')
    maxErtek = pontszamok[0]
    maxIndex = 0
    for i in range(len(pontszamok)):
        if maxErtek < pontszamok[i]:
            maxErtek = pontszamok[i]
            maxIndex = i
    print(f'A legjobb dolgozat sorszáma: {maxIndex+1}, elért pontok száma: {maxErtek}')

    input('\n<Enter>')

def legjobbDolgozat2():
    os.system('cls')
    maxErtek = pontszamok[0]
    maxIndex = 0
    for index, pont in enumerate(pontszamok):
        if maxErtek < pont:
            maxErtek = pont
            maxIndex = index
    print(f'A legjobb dolgozat sorszáma: {maxIndex+1}, elért pontok száma: {maxErtek}')

    input('\n<Enter>')

def eldontes():
    os.system('cls')
    pontszam = int(input('Kérem a pontszámot: '))
    i = 0
    while i < len(pontszamok) and pontszamok[i] != pontszam:
        i += 1
    if i < len(pontszamok):
        print('Van ilyen pontszámú dolgozat')
    else:
        print('Nincs ilyen dolgozat')

    input('\n<Enter>')

def eldontes2():
    os.system('cls')
    pontszam = int(input('Kérem a pontszámot: '))
    
    if pontszamVanE(pontszam):
        print('Van ilyen pontszámú dolgozat')
    else:
        print('Nincs ilyen dolgozat')

    input('\n<Enter>')

def pontszamVanE(pontszam: int) -> bool:
    for pont in pontszamok:
        if pont == pontszam:
            return True
    return False

def nullaPontos():
    os.system('cls')
    i = 0
    while i < len(pontszamok) and pontszamok[i] != 0:
        i += 1
    if i < len (pontszamok):
        print(f'Az első 0 pontos doga a(z) {i+1}. volt.')
    else:
        print('Nincs 0 pontos dolgozat')

    input('\n<Enter>')

main()