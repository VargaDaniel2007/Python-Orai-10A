import os

def menu():
    os.system('cls')
    print("Todo program")
    print('\n1.. Egy szám osztói')
    print('2.. Tökéletes szám')
    print('2.. Tökéletes szám kereső')

    return input("\nVálasszon az alábbi pontokból: ")

def main():
    m = menu()
    match m:
        case '1':
            os.system('cls')
            print('\nEgy szám osztói')
            szam = szamBekeres()
            osztok = ''
            # x = 1       #Osztó folyamatos növeléssel
            # while x <= szam:
            #     if szam % x == 0:
            #         osztok += str(x) + '; '
            #     elif szam == x:
            #         osztok += str(x)
            #     x +=1
            # print(f'\nA szám osztói: {osztok}')

            for i in range(0, szam):
                if szam % (i+1) == 0:
                    osztok += str(oszto(szam, i+1)) + '; '
            print(f'A szám osztói: {osztok}')

        case '2':
            os.system('cls')
            print('\nTökéletes szám')
            szam = szamBekeres()
            szamOsszeg = 0
            for i in range(1, szam):
                if szam % i == 0:
                    szamOsszeg += oszto(szam, i)
            if szam == szamOsszeg:
                print(f'A(z) {szam} tökéletes szám')
            else:
                print(f'A(z) {szam} nem tökéletes szám')

        case '3':
            os.system('cls')
            print('\nTökéletes szám kereső')
            szam = szamBekeres()
            tokeletesSzamok = ''
            x = 0
            while x <= szam:
                if tokeletesSzam(x) == True:
                    tokeletesSzamok += str(x) + '; '
                x += 1
            print(f'Tökéletes számok amiket találtam: {tokeletesSzamok}')


def oszto(szam: int, x: int) -> int:
        if szam % x == 0:
            oszthato = x
            return oszthato
        elif szam == x:
            oszthato = x
            return oszthato
        if szam % x == 0:
            oszthato = x
            return oszthato
    
def szamBekeres():
    return int(input('\nKérem írjon be egy pozitív egész számot: '))

def tokeletesSzam(szam: int) -> bool:
    szamOsszeg = 0
    for i in range(1, szam):
        print(oszto(szam, i))
        szamOsszeg += oszto(szam, i)
    if szam == szamOsszeg:
        return True
    else:
        return False

main()