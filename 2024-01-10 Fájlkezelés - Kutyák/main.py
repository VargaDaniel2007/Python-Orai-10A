from kutya import Kutya
import os

kutyak: list[Kutya] = []
#     Kutya('Bodri', 'puli'),
#     Kutya('Cézár', 'dobermann'),
#     Kutya('Rex', 'német juhász'),
#     Kutya('Béla', 'keverék')


def main():
    betoltesFajlbol()
    v = ''
    while v != '0':
        v = menu()
        match v:
            case '1':
                lista()
            case '2':
                uj()
                mentesFajlba()
            case '3':
                eladas()
                mentesFajlba()
            case '4':
                etetes()
                mentesFajlba()
            case '5':
                futtatas()
                mentesFajlba()

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

    input('\n<Enter>')

def uj():
    os.system('cls')
    nev = ''
    while nev == '':
        nev = input('A kutya neve: ')
    
    fajta = ''
    while fajta == '':
        fajta = input('A kutya fajtája: ')

    k = Kutya(nev, fajta)
    kutyak.append(k)

def eladas():
    k = keres()
    if k != None:
        kutyak.remove(k)
        print('Sikeres eladás')

    # input('\n<Enter>')

def etetes():
    k = keres()
    if k != None:
        try:
            k.eszik()
            print('Nyam-nyam')
        except Exception as e:
            print(e)

    # input('\n<Enter>')

def futtatas():
    k = keres()
    if k != None:
        try:
            k.mozog()
            print('Hhhhhhhh')
        except Exception as e:
            print(e)

    # input('\n<Enter>')

def keres() -> Kutya:
    os.system('cls')
    nev = ''
    while nev == '':
        nev = input('A kutya neve: ')

    i = 0
    while i < len(kutyak) and kutyak[i].nev != nev:
        i += 1
    
    if i < len(kutyak):
        return kutyak[i]
    
    print('Ilyen nevű kutya nincs a listában')
    return None

def betoltesFajlbol():
    f = open('kutyak.txt', 'r', encoding='utf-8')
    f.readline()
    for row in f:
        r = row.strip()
        data = r.split(';')
        kutya = Kutya(nev = data[0], fajta = data[1], eletero = int(data[2]))
        kutyak.append(kutya)

    f.close()

def mentesFajlba():
    f = open('kutyak.txt', 'w', encoding='utf-8')
    f.write('név;fajta;életerő\n')
    for kutya in kutyak:
        # f.write(f'{kutya.nev};{kutya.fajta};{kutya.eletero}\n')
        #VAGY
        f.write('{0};{1};{2}\n'.format(
                kutya.nev, 
                kutya.fajta, 
                kutya.eletero))
    
    f.close()
    print('A változtatás mentve a fájlba..')
    input('<ENTER>')


main()
