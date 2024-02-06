from foglalas import Foglalas

def idopont_kulonbseg(idopont1: str, idopont2: str) -> int:
    ora1, perc1 = idopont1.split(':')
    ora2, perc2 = idopont2.split(':')

    return int(ora1) * 60 + int(perc1) - (int(ora2) * 60 + int(perc2))

foglalasok: list[Foglalas] = []

f = open('fogado.txt', 'r', encoding='utf-8')
for sor in f:
    foglalasok.append(Foglalas(sor))
f.close()

print('2. feladat')
print(f'Foglalások száma: {len(foglalasok)}')

print('3. feladat')
nev = input('Adjon meg egy nevet: ')

db = 0
for f in foglalasok:
    if f.nev == nev:
        db += 1
if db > 0:
    print(f'{nev} néven {db} időpontfoglalás van.')
else:
    print('A megadott néven nincs időpontfoglalás.')

print('4. feladat')
idopont = input('Adjon meg egy érvényes időpontot (pl. 17:10): ')
f = open(f'{idopont.replace(":","")}.txt', 'w', encoding='utf-8')
for fogl in foglalasok:
    if fogl.idopont == idopont:
        print(fogl.nev)
        f.write(f'{fogl.nev}\n')
f.close()

print('5. feladat')
#todo dátum pontosítása
min = foglalasok[0]
for f in foglalasok:
    if f.foglalas_idopont < min.foglalas_idopont:
        min = f
print(f'Tanár neve: {min.nev}\n'
      f'Foglalás időpontja: {min.idopont}\n'
      f'Foglalás ideje: {min.foglalas_idopont}')

print('6. feladat')
lehetseges_idopontok = ['16:00', '16:10', '16:20', '16:30', '16:40', '16:50',
                        '17:00', '17:10', '17:20', '17:30', '17:40', '17:50']
for f in foglalasok:
    if f.nev == 'Barna Eszter':
        lehetseges_idopontok.remove(f.idopont)
for i in lehetseges_idopontok:
    print(i)

if lehetseges_idopontok[-1] != '17:50':
    print('Barna Eszter legkorábban távozhat: 18:00')
else:
    for i in range(len(lehetseges_idopontok)-1, -1, -1):    #Ha hossz pl: 5
        if i == 0 or idopont_kulonbseg(lehetseges_idopontok[i], lehetseges_idopontok[i-1]) > 10:
            print(f'Barna Eszter legkorábban távozhat: {lehetseges_idopontok[i]}')
            break