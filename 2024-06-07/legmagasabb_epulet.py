from epulet import Epulet

epuletek: list[Epulet] = []

f = open('legmagasabb.txt', 'r', encoding='utf-8')
f.readline()
for sor in f:
    epuletek.append(Epulet(sor))
f.close()

print(f'3.2 feladat: Épületek száma: {len(epuletek)} db')

ossz = 0
for e in epuletek:
    ossz += e.emelet

print(f'3.3 feladat: Emeletek összege: {ossz}')

legmagasabb: Epulet = epuletek[0]

for e in epuletek[1:]:
    if legmagasabb.magassag < e.magassag:
        legmagasabb = e
    
print(f'3.4 feladat: A legmagasabb épület adatai')
print(f'\tNév: {legmagasabb.nev}'
      f'\n\tVáros: {legmagasabb.varos}'
      f'\n\tOrszág: {legmagasabb.orszag}'
      f'\n\tMagasság: {legmagasabb.magassag} m'
      f'\n\tEmeletek száma: {legmagasabb.emelet}'
      f'\n\tÉpítés éve: {legmagasabb.epult}')

i = 0
while i < len(epuletek) and epuletek[i].orszag != 'Olaszország':
    i += 1

if i < len(epuletek):
    print('3.5 feladat: Van olasz épület az adatok között!')
else:
    print('3.5 feladat: Nincs olasz épület az adatok között!')

