from fizetes import Fizetes

fizetesek: list[Fizetes] = []
#1. feladat
f = open('fizetesek.csv', 'r', encoding='utf-8')
f.readline()
for sor in f:
    fizetesek.append(Fizetes(sor))
f.close()

#2. feladat
print(f'2. feladat: A cégnél {len(fizetesek)} munkavállaló dolgozik.')

#3. feladat
bekert_nev = input('3. feladat: Dolgozó neve: ')

#4. feladat
i = 0
while i < len(fizetesek) and fizetesek[i].nev != bekert_nev:
    i += 1
if i < len(fizetesek):
    print(f'4. feladat: A dolgozó fizetése: {fizetesek[i].fizetes} Ft.')
else:
    print('4. feladat: Ilyen nevű dolgozó nincs a cégnél.')

# 5. feladat
max: Fizetes = fizetesek[0]
for fi in fizetesek[1:]:
    if fi.fizetes > max.fizetes:
        max = fi
print(f'5. feladat: A legjobban kereső dolgozó: {max.nev}, fizetése: {max.fizetes} Ft.')

#6/1. feladat
ossz_fiz = 0
for fi in fizetesek:
    ossz_fiz += fi.fizetes
atl_fiz = ossz_fiz / len(fizetesek)

#6/2. feladat
print(f'6. feladat: Az átlagnál ({atl_fiz:.0f} Ft) kevesebbet kereső dolgozók:')
for fi in fizetesek:
    if fi.fizetes < atl_fiz:
        print(f'\t{fi.nev}')

#7. feladat
f = open('fizetesek_uj.csv', 'w', encoding='utf-8')
f.write('Név;Új fizetése\n')
for fi in fizetesek:
    f.write(f'{fi.nev};{fi.fizetes*1.2:.0f}\n')
f.close()