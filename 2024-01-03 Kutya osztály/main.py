from kutya import Kutya
import os

kutyak: list[Kutya] = [
    Kutya('Bodri', 'puli'),
    Kutya('Cézár', 'dobermann'),
    Kutya('Rex', 'német juhász'),
    Kutya('Béla', 'keverék')
]

def main():
    v = ''
    while v != '0':
        v = menu()
        match v:
            case '1':
                lista()
            case '2':
                uj()
            case '3':
                eladas()
            case '4':
                etetes()
            case '5':
                futtatas()            
def menu():
    os.system('cls')
    print('1..Kutyák listája')
    print('2..Új kutya')
    print('3..Kutya eladása')
    print('4..Kutya etetése')
    print('5..Kutya futtatása')
    print('0..Kilépés')
    return input('\nVálasztás: ')

def lista():
    os.system('cls')
    for k in kutyak:
        print(f'{k.nev}: {k.fajta}, {k.allapot()}')
    input('\n<ENTER>')

def uj():
    os.system('cls')
    nev  = ''
    while nev == '':        #HF Ha van már a név akkor kérjen újat
        nev = input('A kutya neve: ')

    fajta  = ''
    while fajta == '':
        fajta = input('A kutya fajtája: ')

    k = Kutya(nev, fajta)
    kutyak.append(k)

def eladas():
    k = keres()
    if k != None:
        kutyak.remove(k)
        print('Sikeres eladás')

    input('\n<ENTER>')

def etetes():
    k = keres()
    if k != None:
        try:
            k.eszik()
            print('Az eb evett')
        except Exception as e:
            print(e)
    
    input('\n<ENTER>')

def futtatas():
    k = keres()
    if k != None:
        try:
            k.mozog()
            print('Az eb mozgott')
        except Exception as e:
            print(e)

    input('\n<ENTER>')        

def keres() -> Kutya:
    os.system('cls')
    nev  = ''
    while nev == '':
        nev = input('A kutya neve: ')
    
    i = 0
    while i < len(kutyak) and kutyak[i].nev != nev:
        i += 1
    if i < len(kutyak):
        return kutyak[i]
    
    print('Ilyen nevű kutya nincs a listában')
    return None

main()