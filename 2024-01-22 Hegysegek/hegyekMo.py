from hegycsucs import Hegycsucs

csucsok: list[Hegycsucs] = []

f = open('hegyekMo.txt', 'r', encoding='utf-8')
f.readline()
for sor in f:
    csucsok.append(Hegycsucs(sor))
f.close()

print(f'3. feladat: Hegycsúcsok száma: {len(csucsok)} db')

ossz = 0
for cs in csucsok:
    ossz += cs.magassag

print(f'4. feladat: Hegycsúcsok átlagos magassága: {ossz / len(csucsok):.1f} m')

legmagasabb: Hegycsucs = csucsok[0]
for cs in csucsok:
    if cs.magassag > legmagasabb.magassag:
        legmagasabb = cs

print('5. feladat: A legmagasabb csúcs adatai:')
print(f'\tNév: {legmagasabb.nev}')
print(f'\tHegység: {legmagasabb.hegyseg}')
print(f'\tMagasság: {legmagasabb.magassag}')

m = int(input('6. feladat: Kérek egy magasságot: '))
i = 0
while i < len(csucsok) and csucsok[i].magassag < m:
    i += 1
if i < len(csucsok):
    print(f'Van {m} méternél magasabb hegycsúcs, pl a: {csucsok[i].nev}')
else:
    print(f'Nincs {m} méternél magasabb hegycsúcs')

db = 0
for cs in csucsok:
    if cs.magassag * 3.280839895 > 3000:
        db += 1
print(f'7. feladat: 3000 lábnál magasabb hegycsúcsok száma: {db}')

f = open('bukk-videk.txt', 'w', encoding='utf-8')
for cs in csucsok:
    if cs.hegyseg == 'Bükk-vidék':
        # f.write(f'{cs.nev};{cs.magassag * 3.280839895:.1f}\n')
        f.write(f'{cs.nev};{floor(cs.magassag * 3.280839895 * 10 + 0.5) / 10}\n')

f.close()

