import os
from auto import Auto

autok: list[Auto] = []

def main():
    # induloAdatok()
    v = ''
    while v != '0':
        v = menu()
        match v:
            case '1':
                autoLista()
            case '2':
                ujAuto()
            case '3':
                autoTorles()
            case '4':
                ujUt()
            case '5':
                pass
            case '6':
                betoltesFajlbol()
            case '7':
                mentesFajlba()

def menu() -> str:
    os.system('cls')
    print('1..Autók listája')
    print('2..Új autó rögzítése / beszerzése')
    print('3..Autó törlése / eladása')
    print('4..Megtett út rögzítése')
    print('5..Tankolás rögzítése')
    print('6..Adatok betöltése')
    print('7..Adatok mentése')
    print('0..Kilépés')

    return input('\nVálasztás: ')

'''
def induloAdatok():
    audi = Auto()    # példányosítás
    audi.rendszam = 'ABC-123'
    audi.tipus = 'Audi RS6'
    audi.fogyasztas = 14.5
    audi.kmOraAllas = 23245
    audi.uzemanyagMennyiseg = 23.5
    audi.uzemanyagTartalyMeret = 73    

    autok.append(audi)

    vw = Auto()    
    vw.rendszam = 'DEF-456'
    vw.tipus = 'Vw Passat 1.9TDI'
    vw.fogyasztas = 7.5
    vw.kmOraAllas = 122542
    vw.uzemanyagMennyiseg = 3.4
    vw.uzemanyagTartalyMeret = 68

    # autok.append(Auto('XYZ-987', 'Lada 1200', 9.7, 121234, 9, 42))

    autok.append(vw)
'''

def autoLista():
    os.system('cls')
    for a in autok:        
        print(a.rendszam)
        print(f'\t{a.tipus}, {a.kmOraAllas} km, {a.fogyasztas} l/100km, {a.uzemanyagMennyiseg}/{a.uzemanyagTartalyMeret} l')

    input('<ENTER>')

def ujAuto():
    os.system('cls')    
    rendszam = input('Az új autó rendszáma: ')
    tipus = input('Típusa: ')
    kmOraAllas = int(input('Km óra állása: '))
    fogyasztas = float(input('Fogyasztása (liter / 100km): '))
    uzemanyagTartalyMeret = int(input('Üzemanyag tartály mérete (l): '))
    uzemanyagMennyiseg = float(input('Jelenlegi üzemanyag szint/mennyiség (l): ')) #TODO: ellenőrzés

    autok.append(Auto(rendszam, tipus, kmOraAllas, fogyasztas, uzemanyagMennyiseg, uzemanyagTartalyMeret))
    print('\nSikeres rögzítés')
    input('<ENTER>')

def autoKereses(szoveg: str) -> Auto:
    rendszam = input(szoveg)
    i = 0
    while i < len(autok) and autok[i].rendszam != rendszam:
        i += 1
    if i < len(autok):
        return autok[i]
    return None

def autoTorles():
    os.system('cls')
    a = autoKereses("Kérem a törlendő autó rendszámát: ")
    if a == None:
        print('Az autó nem található')
    else:
       autok.remove(a) 
       print('Sikeres törlés')

    input('<ENTER>')

def ujUt():
    os.system('cls')
    a = autoKereses("Kérem az autó rendszámát: ")
    if a == None:
        print('Az autó nem található')
    else:
        ujKmOraAllas = int(input('Az autó km óra állása az út után: '))
        try:
            a.utazas(ujKmOraAllas)
            print('Sikeres rögzítés')
        except Exception as e:            
            print(e)
        
    input('<ENTER>')

def betoltesFajlbol():
    os.system('cls')
    f = open('autok.txt', 'r', encoding='utf-8')
    f.readline()
    for row in f:
        r = (row.strip())   # r='ABC-123;Audi RS6;23245;14.5;23.5;73'
        data = r.split(';') # data=['ABC-123','Audi RS6','23245','14.5','23.5','73']
        auto = Auto(rendszam= data[0],
                    tipus= data[1],
                    kmOraAllas= int(data[2]),
                    fogyasztas= float(data[3]),
                    uzemanyagMennyiseg= float(data[4]),
                    uzemanyagTartalyMeret= int(data[5]))
        autok.append(auto)
    f.close()
    
    print('Sikeres betöltés...')
    input('<ENTER>')

def mentesFajlba():
    os.system('cls')
    f = open('autok.txt', 'w', encoding='utf-8')
    
    f.write('rendszám;típus;km óra állás;fogyasztás;üa mennyiség;üa tartály mérete\n')
    for auto in autok:
        f.write(f'{auto.rendszam};{auto.tipus};{auto.kmOraAllas};{auto.fogyasztas};' +
              f'{auto.uzemanyagMennyiseg};{auto.uzemanyagTartalyMeret}\n')

    f.close()
    print('Sikeres mentés...')
    input('<ENTER>')

main()
