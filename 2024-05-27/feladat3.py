from festmeny import Festmeny
festmenyek : list[Festmeny] = []

f = open('paintings.txt', 'r', encoding='UTF-8')
f.readline()
for sor in f:
    festmenyek.append(Festmeny(sor))
f.close()

print(f'3.3 feladat: A fájlban tárolt festmények száma: {len(festmenyek)}')

ossz = 0
for p in festmenyek:
    if p.festo == 'Pablo Picasso':
        ossz += 1
print(f'A Pablo Picasso képek száma: {ossz} darab.')

maxKep: Festmeny = festmenyek[0]
for p in festmenyek[1:]:
    if maxKep.becsult_ertek < p.becsult_ertek:
        maxKep = p
print(f'A legdrágább kép festője: {maxKep.festo}, a kép címe {maxKep.festmeny}, becsült értéke: {maxKep.becsult_ertek} dollár.')

i = 0
while i < len(festmenyek) and festmenyek[i].becsult_ertek > festmenyek[i].eredeti_ar:
    i += 1
if i < len(festmenyek):
    print('3.6 feladat: Van olyan festmény, amelynek a becsült értéke nem haladja meg az eredeti árát.')
else:
    print('3.6 feladat: Nincs olyan festmény, amelynek a becsült értéke nem haladja meg az eredeti árát.')