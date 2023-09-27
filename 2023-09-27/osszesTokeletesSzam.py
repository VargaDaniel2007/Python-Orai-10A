maxSzam = int(input('Tökéletes szám keresésének felső határa: '))

print('Ezeket a tökéletes számokat találtam:')

for szam in range(1, maxSzam + 1):
    osszeg = 0
    for i in range(1, szam):
        if szam % i == 0:
            osszeg += i

    if osszeg == szam:
        print(szam, end='; ')
