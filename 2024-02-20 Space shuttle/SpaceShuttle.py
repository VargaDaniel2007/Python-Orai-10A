from kuldetes import Kuldetes

kuldetesek: list[Kuldetes] = []

f = open('kuldetesek.csv', 'r', encoding='utf-8')
for sor in f:
    kuldetesek.append(Kuldetes(sor))
f.close()

print('3. feladat')
print(f'\tÖsszesen {len(kuldetesek)} alkalommal indítottak űrhajót.')

print('4. feladat')
ossz = 0
for k in kuldetesek:
    ossz += k.legenyseg
print(f'\t{ossz} utas indult az űrbe összesen.')

print('5. feladat')
db = 0
for k in kuldetesek:
    if k.legenyseg < 5:
        db += 1
print(f'\tÖsszesen {db} alkalommal küldtek kevesebb, mint 5 embert az űrbe.')

print('6. feladat')
i = 0
while i < len(kuldetesek) and (kuldetesek[i]. ursiklo != 'Columbia' or kuldetesek[i].landolas != 'nem landolt'):
    i += 1
if i < len(kuldetesek):
    print(f'\t{kuldetesek[i].legenyseg} asztronauta volt a Columbia fedélzetén annak utolsó útján')
else:
    print('\tAz állományban nem szerepel a Columbia utolsó útja')

print('7. feladat')
leghosszabb: Kuldetes = kuldetesek[0]
for k in kuldetesek:
    if k.osszes_ora > leghosszabb.osszes_ora:
        leghosszabb = k

print(f'\tA leghosszabb ideig a {leghosszabb.ursiklo} volt az űrben {leghosszabb.kod} küldetés során')
print(f'\tÖsszesen {leghosszabb.osszes_ora} órát volt távol a Földtől')

print('8. feladat')
evszam = input('\tÉvszám: ')
db = 0
for k in kuldetesek:
#     if k.datum.startswith(evszam):
#         db += 1
    if  k.datum[:4] == evszam:
        db += 1
if db == 0:
    print('\tEbben az évben nem indult küldetés')
else:
    print(f'\tEbben az évben {db} küldetés volt')

print('9. feladat')
db = 0
for k in kuldetesek:
    if k.landolas == 'Kennedy':
        db += 1
print(f'\tA küldetések {100 * db /len(kuldetesek):.2f} %-a fejeződött be a Kennedy űrközpontban.')

stat = dict()
for k in kuldetesek:
    if k.ursiklo in stat.keys():
        stat[k.ursiklo] += k.osszes_ora
    else:
        stat[k.ursiklo] = k.osszes_ora

f = open('ursiklok.txt', 'w', encoding='utf-8')
for key, value in stat.items():
    f.write(f'{key}\t{value/24:.2f}\n')
f.close()