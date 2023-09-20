import os, random

def main() -> None:
    #"Főprogram" függvénye
    egyenleg = 1000
    m = ''
    while m != '0':
        informacio(egyenleg)
        m = menu()
        match m:

            case '1':
                tet = osszegBekeres(egyenleg)
                szam = sorsolas()
                if szam == 0 or szam % 2 == 1:
                    egyenleg -= tet
                    print(f'VESZTETT, az új egyenlege: {egyenleg}')

                else:
                    egyenleg += tet
                    print(f'Nyert, az új egyenlege: {egyenleg}')
                input('\n\nENTER')
            
            case '2':
                tet = osszegBekeres(egyenleg)
                szam = sorsolas()
                if szam % 2 == 0:
                    egyenleg -= tet
                    print(f'VESZTETT, az új egyenleg: {egyenleg}')
                else:
                    egyenleg += tet
                    print(f'Nyert, az új egyenlege: {egyenleg}')
                input('\n\nENTER')

            case '3':
                tet = osszegBekeres(egyenleg)
                szam = sorsolas()
                if szam == 0 or szam > 18:
                    egyenleg -= tet
                    print(f'VESZTETT, az új egyenleg: {egyenleg}')
                else:
                    egyenleg += tet
                    print(f'Nyert, az új egyenleg: {egyenleg}')
                input('\n\nENTER')

            case '4':
                tet = osszegBekeres(egyenleg)
                szam = sorsolas()
                if szam < 19:
                    egyenleg -= tet
                    print(f'VESZTETT, az új egyenleg: {egyenleg}')
                else:
                    egyenleg += tet
                    print(f'Nyert, az új egyenleg: {egyenleg}')
                input('\n\nENTER')
            
            case '5':       #TUCATOK
                tm = ''
                while tm != '0':
                    informacio(egyenleg)
                    tm = tucatMenu()
                    match tm:

                        case '1':       #1-12
                            tet = osszegBekeres(egyenleg)
                            szam = sorsolas()
                            if szam == 0 or szam > 13:
                                egyenleg -= tet
                                print(f'VESZTETT, az új egyenleg: {egyenleg}')
                            else:
                                egyenleg += tet*2
                                print(f'Nyert, az új egyenleg: {egyenleg}')
                            input('\nENTER')

                        case '2':       #13-24
                            tet = osszegBekeres(egyenleg)
                            szam = sorsolas()
                            if szam < 13 or szam > 24:
                                egyenleg -= tet
                                print(f'VESZTETT, az új egyenleg: {egyenleg}')
                            else:
                                egyenleg += tet*2
                                print(f'Nyert, az új egyenleg: {egyenleg}')
                            input('\nENTER')

                        case '3':       #25-36
                            tet = osszegBekeres(egyenleg)
                            szam = sorsolas()
                            if szam < 25:
                                egyenleg -= tet
                                print(f'VESZTETT, az új egyenleg: {egyenleg}')
                            else:
                                egyenleg+= tet*2
                                print(f'Nyert, az új egyenleg: {egyenleg}')
                            input('\nENTER')

            case '6':       #OSZLOPOK
                om = ''
                while om != '0':
                    informacio(egyenleg)
                    om = oszlopMenu()
                    match om:

                        case '1':       #. Oszlop
                            tet = osszegBekeres(egyenleg)
                            szam = sorsolas()
                            if szam % 3 != 1:
                                egyenleg -= tet
                                print(f'VESZTETT, az új egyenleg: {egyenleg}')
                            else:
                                egyenleg += tet*2
                                print(f'Nyert, az új egyenleg: {egyenleg}')
                            input('\nENTER')

                        case '2':       #2. Oszlop
                            tet = osszegBekeres(egyenleg)
                            szam = sorsolas()
                            if szam % 3 != 2:
                                egyenleg -= tet
                                print(f'VESZTETT, az új egyenleg: {egyenleg}')
                            else:
                                egyenleg += tet*2
                                print(f'Nyert, az új egyenleg: {egyenleg}')
                            input('\nENTER')
                        case '3':
                            tet = osszegBekeres(egyenleg)
                            szam = sorsolas()
                            if szam % 3 != 0:
                                egyenleg -= tet
                                print(f'VESZTETT, az új egyenleg: {egyenleg}')
                            else:
                                egyenleg += tet*2
                                print(f'Nyert, az új egyenleg: {egyenleg}')
                            input('\nENTER')

            case '7':
                tet = osszegBekeres(egyenleg)
                bekertszam = szamBekeres()
                szam = sorsolas()
                if szam != bekertszam:
                    egyenleg -= tet
                    print(f'VESZTETT, az új egyenleg: {egyenleg}')
                else:
                    egyenleg += tet*35
                    print(f'Nyert, az új egyenleg: {egyenleg}')
                input('\nENTER')

            case '8':
                tet = osszegBekeres(egyenleg)
                szam = sorsolas()
                if piros(szam) == True:
                    egyenleg += tet
                    print(f'Nyert, az új egyenleg: {egyenleg}')
                else:
                    egyenleg -= tet
                    print(f'VESZTETT, az új egyenleg: {egyenleg}')
                input('\nENTER')
            
            case '9':
                tet = osszegBekeres(egyenleg)
                szam = sorsolas()
                if piros(szam) == False:
                    egyenleg += tet
                    print(f'Nyert, az új egyenleg: {egyenleg}')
                else:
                    egyenleg -= tet
                    print(f'VESZTETT, az új egyenleg: {egyenleg}')
                input('\nENTER')


def informacio(penz: int) -> None:
    os.system('cls')
    # \t => tabulátor
    print(f'Rulett játék \t\t\t Jelenlegi egyenleg: {penz} krajcár')
    
def menu() -> int:
    # \n => sortörés
    print('\n')

    print("1..Tét: Páros")
    print("2..Tét: Páratlan")
    print("3..Tét: 1-18")
    print("4..Tét: 19-36")
    print("5..Tét: Tucatok")
    print("6..Tét: Oszlopok")
    print("7..Tét: Szám")
    print("8..Tét: Piros")
    print("9..Tét: Fekete")
    # print()
    # print("0..Kilépés")
    print('\n0..Kilépés')

    return input('\nVálasztás: ')

def tucatMenu() -> int:
    print('\n')

    print("1.. Tucat: 1-12")
    print("2.. Tucat: 13-24")
    print("3.. Tucat: 25-36")

    print('\n0.. Kilépés')

    return input('\nVálasztás: ')

def oszlopMenu() -> int:
    print('\n')

    print("1.. 1. Oszlop")
    print("2.. 2. Oszlop")
    print("3.. 3. Oszlop")

    print('\n0.. Kilépés')

    return input('\nVálasztás: ')

def osszegBekeres(maxOsszeg: int) -> int:
    osszeg = 0
    while osszeg <= 0 or osszeg > maxOsszeg:
        informacio(maxOsszeg)
        osszeg = int(input("Mekkora összeget tesz fel? "))
    return osszeg

def szamBekeres() -> int:
    return input('\nA szám amire a tétet akarja tenni: ')

def sorsolas() -> int:
    szam = random.randint(0, 36)
    print(f'\n\nA "gurított" szám: {szam}')
    return szam

def piros(szam: int) -> bool:
    if szam == 1:
        return True
    elif szam == 3:
        return True
    elif szam == 5:
        return True
    elif szam == 7:
        return True
    elif szam == 9:
        return True
    elif szam == 12:
        return True
    elif szam == 14:
        return True
    elif szam == 16:
        return True
    elif szam == 18:
        return True
    elif szam == 19:
        return True
    elif szam == 21:
        return True
    elif szam == 23:
        return True
    elif szam == 25:
        return True
    elif szam == 27:
        return True
    elif szam == 30:
        return True
    elif szam == 32:
        return True
    elif szam == 34:
        return True
    elif szam == 36:
        return True
    else:
        return False


main()