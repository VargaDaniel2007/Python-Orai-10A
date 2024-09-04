from cbadas import CBadas

adasok: list[CBadas] = []

f = open('cb.txt', 'r', encoding='UTF-8')
f.readline()
for sor in f:
    adasok.append(CBadas(sor))
f.close()

print('3. feladat: CB-Rádió')
print(f'3.2 feladat: Bejegyzések száma: {len(adasok)} db')

ossz = 0
for a in adasok:
    if a.nev == 'Sanyi':
        ossz += 1

print(f'3.3 feladat: Sanyihoz tartozó bejegyzések: {ossz} db')

top: list[CBadas] = [adasok[0]]

for a in adasok:
    if a.adasdb > top[0].adasdb:
        top.clear()
        top.append(a)
    elif a.adasdb == top[0].adasdb:
        top.append(a)
    
print('3.4 feladat: A legtöbb adás:')
for t in top:
    print(f'\tIdő: {t.ora}:{t.perc} Darab: {t.adasdb} Név: {t.nev}')


f = open('cb2.txt', 'w', encoding='UTF-8')
f.write('Kezdes;Nev;AdasDb\n')
for a in adasok:
    f.write(f'{a.ora*24+a.perc};{a.nev};{a.adasdb}\n')