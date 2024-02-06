from foglalas import Foglalas

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