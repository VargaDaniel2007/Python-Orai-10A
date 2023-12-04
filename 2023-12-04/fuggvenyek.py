from os import system
korIdo = ['1:36.103', '1:57.799', '1:41.153', '1:51.697', '1:40.370', '1:36.106', '1:52.216', '1:40.766', '1:57.311', '1:39.668', '1:46.402', '1:59.298', '1:47.474', '1:44.234', '1:49.676', '1:57.474', '1:49.263', '1:36.397']

def masodperc(korido: str) -> float:
    #pl.: 1:36.103
    if korido != float:
        ido = korido.split(':')             #Listává választja a megadott karakter mentén: ['1', '36.103']
    
    return int(ido[0]) * 60 + float(ido[1])

def ujKorIdo():
    system('cls')
    print('Új köridő hozzáadása \n\n')

    sorszam = int(input('Hányas sorszámú versenyző idejét írná be: '))
    pluszKorIdo_str = input(f'Mekkora az új körideje a {sorszam}. sorszámú versenyzőnek (m:ss.sss): ')
    pluszKorIdo = masodperc(pluszKorIdo_str)
    if sorszam > len(korIdo):
        korIdo.append(pluszKorIdo_str)
        print(f'A {sorszam}. sorszámú versenyző új körideje: {pluszKorIdo_str}')
        input('\nEnter...')
    else:
        if masodperc(korIdo[sorszam-1]) <= pluszKorIdo:
            print('\n A versenyzőnek már van gyorsabb körideje.')
            input('\nEnter...')
        else:
            korIdo[sorszam-1] = pluszKorIdo
            print(f'A {sorszam}. sorszámú versenyző új leggyorsabb köre: {pluszKorIdo_str}')
            input('\nEnter...')

def nyertes():
    system('cls')
    minIndex = 0
    minErtek = masodperc(korIdo[0])
    for i in range(1, len(korIdo)):
        if masodperc(korIdo[i]) < minErtek:
            minIndex = i
            minErtek = masodperc(korIdo[i])
    print(f'Leggyorsabb versenyző: {minIndex+1}, körideje: {korIdo[minIndex]}')
    input('\nEnter...')