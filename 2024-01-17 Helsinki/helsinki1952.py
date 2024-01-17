from olimpia import Helyezes

helyezesek: list[Helyezes] = []

def main():
    beolvasas()
    pontszerzo()
    erem()
    olimpiaPontOsszes()
    legtobbErem()
    kajakJavitas()
    legtobbSportolo()



def beolvasas():
    f = open('helsinki.txt', 'r', encoding='utf-8')
    for sor in f:
        helyezesek.append(Helyezes(sor))
    f.close()

def pontszerzo():
    db = 0
    for hely in helyezesek:
        if hely.helyezes <= 6:
            db += 1
    print( '3. feladat:\n'
          f'Pontszerző helyezések száma: {db}')

def erem():
    dbar = 0
    dbez = 0
    dbbro = 0
    for hely in helyezesek:
        match hely.helyezes:
            case 1:
                dbar += 1
            case 2:
                dbez += 1
            case 3:
                dbbro += 1
    print('4. feladat:\n'
         f'Arany: {dbar}\n'
         f'Ezüst: {dbez}\n'
         f'Bronz: {dbbro}\n'
         f'Összesen: {dbar+dbez+dbbro}')
    
def olimpiaPontOsszes():
    pont = 0
    for hely in helyezesek:
        match hely.helyezes:
            case 1:
                pont += 7
            case 2:
                pont += 5
            case 3:
                pont += 4
            case 4:
                pont += 3
            case 5:
                pont += 2
            case 6:
                pont += 1
    print('5. feladat')
    print(f'Olimpiai pontok száma: {pont}')
            
def legtobbErem():
    uszaserem = 0
    tornaerem = 0
    for hely in helyezesek:
        match hely.sportag:
            case 'uszas':
                if hely.helyezes <= 3:
                    uszaserem += 1
            case 'torna':
                    tornaerem += 1
    print('6.feladat')
    if uszaserem == tornaerem:
        print('Egyenlő volt az érmek száma')
    elif uszaserem > tornaerem:
        print('Úszás sportágban szereztek több érmet')
    else:
        print('Torna sportágban szereztek több érmet')
        
def kajakJavitas():
    f = open('helsinki2.txt', 'w', encoding='utf-8')  
    for hely in helyezesek:
        if hely.sportag == 'kajakkenu':
            f.write(f'{hely.helyezes} {hely.sportolok} {olimpiaPont(hely)} kajak-kenu {hely.versenysz}\n')
        else:
            f.write(f'{hely.helyezes} {hely.sportolok} {olimpiaPont(hely)} {hely.sportag} {hely.versenysz}\n')
    f.close()

def olimpiaPont(hely: Helyezes) -> str:
        match hely.helyezes:
            case 1:
                return '7'
            case 2:
                return '5'
            case 3:
                return '4'
            case 4:
                return '3'
            case 5:
                return '2'
            case 6:
                return '1'

def legtobbSportolo():
    legtobbIndex = 0
    legtobb = helyezesek[0].sportolok
    for i in range(1, len(helyezesek)):
        if helyezesek[i].sportolok > legtobb:
            legtobbIndex = i
            legtobb = helyezesek[i].sportolok
    print('8. feladat:\n'
         f'Helyezés: {helyezesek[legtobbIndex].helyezes}\n'
         f'Sportág: {helyezesek[legtobbIndex].sportag}\n'
         f'Versenyszám: {helyezesek[legtobbIndex].versenysz}\n'
         f'Sportolók száma: {helyezesek[legtobbIndex].sportolok}\n')
        


main()