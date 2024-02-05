from het import Het

def print_szamok(szamok: list[int]):
    for szam in szamok:
        print(f'\t{szam}', end='')

print('1. feladat: az 52. hét számai')
szamok52: list[int] = []
for i in range(1, 6):
    szamok52.append( int(input(f'\t{i}. szám: ')) )

szamok52.sort()

print(f'2. feladat')
print_szamok(szamok52)

print('\n3.feladat')

hetek: list[Het] = []

f = open('lottosz.txt', 'r')
for sor in f:
    hetek.append(Het(sor))
f.close()

het_szam =  int(input('\tKérem a hetet: '))

print(f'4. feladat: A {het_szam} hét nyerőszámai:')
print_szamok(hetek[het_szam - 1].szamok)

osszes_szam: list[int] = []
for i in range(1, 91):
    osszes_szam.append(i)

for het in hetek:
    for szam in het.szamok:
        if szam in osszes_szam:
            osszes_szam.remove(szam)
print('5. feladat:')
if len(osszes_szam) == 0:
    print('\tNem volt olyan szám amit nem húztak ki')
else:
    print('\tVotl(ak) olyan szám(ok) ami(ke)t nem húztak ki')