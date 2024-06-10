from fogadasi_het import Fogadasi_fordulo

print('3. feladat: Toto')

print('3.1 feladat: Adatok beolvasása és tárolása')
fogadasok: list[Fogadasi_fordulo] = []

f = open('források/3. feladat/toto.txt', 'r', encoding='UTF-8')
f.readline()
for sor in f:
    fogadasok.append(Fogadasi_fordulo(sor))

f.close()

print(f'3.2 feladat: Fogadási fordulók száma: {len(fogadasok)}')

ossz = 0
for f in fogadasok:
    ossz += f.t13p1

print(f'3.3 feladat: Telitalálatos szelvények száma: {ossz} darab')

i = 0
while i < len(fogadasok) and 'X' in fogadasok[i].eredmenyek:
    i += 1

if i < len(fogadasok):
    print('3.4 feladat: Volt döntetlen mentes forduló!')
else:
    print('3.4 feladat: Nem volt döntetlen mentes forduló!')