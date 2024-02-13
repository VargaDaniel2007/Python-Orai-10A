from uzenet import Uzenet

uzenetek: list[Uzenet] = []

def main():
    beolvasas()
    utolso_uzenet_a_telefonban()
    leghosszabb_es_legrovidebb_uzenet()
    statisztika()
    szolgaltato_uzenet_darab()
    baratno_uzenetei()
    smski()

def beolvasas() -> int:
    f = open('sms.txt', 'r', encoding='utf-8')
    uzenetek_szam = int(f.readline())
    for i in range(uzenetek_szam):
        sor1 = f.readline()
        sor2 = f.readline()
        uzenetek.append(Uzenet(sor1, sor2))
    f.close()

    return uzenetek_szam

def utolso_uzenet_a_telefonban():
    print('2. feladat')
    if len(uzenetek) > 10:
        uzenet = uzenetek[9]
    else:
        uzenet = uzenetek[-1]
    print_uzenet(uzenet)

def leghosszabb_es_legrovidebb_uzenet():
    leghosszabb_uzenet = uzenetek[0]
    legrovidebb_uzenet = uzenetek[0]
    for u in uzenetek[1:]:
        if len(u.uzenet) > len(leghosszabb_uzenet.uzenet):
            leghosszabb_uzenet = u
        if len(u.uzenet) < len(legrovidebb_uzenet.uzenet):
            legrovidebb_uzenet = u
    
    print('3. feladat:')
    print('\tLeghosszabb üzenet:')
    print_uzenet(leghosszabb_uzenet)
    print('\tLegrövidebb üzenet:')
    print_uzenet(legrovidebb_uzenet)

def statisztika():
    stat  = dict()
    for u in uzenetek:
        kategoria = u.uzenet_hossz_kategoria()
        if kategoria in stat.keys():
            stat[kategoria] += 1
        else:
            stat[kategoria] = 1

    print('4. feladat')
    for key, value in stat.items():
        print(f'\t{key}: {value} db')

def szolgaltato_uzenet_darab():
    stat = dict()
    for u in uzenetek:
        if u.ora in stat.keys():
            stat[u.ora] += 1
        else:
            stat[u.ora] = 1
    
    db = 0
    #for key, value in stat.items():
    for value in stat.values():
        if value > 10:
            db += (value-10)
    
    print(f'5. feladat: {db} db a feltételnek megfelelő üzenet lennne.')

def baratno_uzenetei():
    uzenetek_baratno: list[int] = []

    for u in uzenetek:
        if u.telefonszam == '123456789':
            uzenetek_baratno.append(u.ora * 60 + u.perc)

    print('6. feladat')
    if len(uzenetek_baratno) < 2:
        print('\t Nincs elegendő üzenet')
    else:
        ido = uzenetek_baratno[1] - uzenetek_baratno[0]
        for i in range(2, len(uzenetek_baratno)):
            if uzenetek_baratno[i] - uzenetek_baratno[i-1] > ido:
                ido = uzenetek_baratno[i] - uzenetek_baratno[i-1]

    ora =  int(ido / 60) 
    perc = ido % 60

    print(f'A leghosszabb idő két üzenet között: {ora} óra {perc} perc')

def smski():
    szamok: list[str] = []
    for u in uzenetek:
        if u.telefonszam not in szamok:
            szamok.append(u.telefonszam)
    
    szamok.sort()

    f= open('smski.txt', 'w', encoding='utf-8')
    for szam in szamok:
        f.write(f'{szam}\n')
        for u in uzenetek:
            if u.telefonszam == szam:
                f.write(f'{u.ora} {u.perc} {u.uzenet}\n')
    
    f.close()




def print_uzenet(uzenet: Uzenet):
    print(f'\t{uzenet.ora}:{uzenet.perc} {uzenet.telefonszam}')
    print(f'\t{uzenet.uzenet}')


#HF Üzenet beírás 7. feladat
    

    
main()