from allat import Allat

allatok: list[Allat] = []

for i in range(0, 3):
    bekert_fajnev = input('Add meg egy állatfaj nevét! ')
    bekert_tomeg = int(input('Hány kilogramm a tömege egy példánynak? '))
    allatok.append(Allat(bekert_fajnev, bekert_tomeg))

for a in allatok:
    print(f'A(z) {a.fajnev} tömege {a.tomeg} kg.')

legnehezebb: Allat = allatok[0]
for a in allatok[1:]:
    if a.tomeg > legnehezebb.tomeg:
        legnehezebb = a

f = open('legnehezebb.txt', 'w', encoding='utf-8')
f.write(legnehezebb.fajnev)
f.close()