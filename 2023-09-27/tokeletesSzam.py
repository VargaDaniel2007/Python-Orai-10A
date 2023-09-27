szam = int(input('Írj be egy pozitív egész számot:'))

osszeg = 0
for i in range(1, szam):
    if szam % i == 0:
        osszeg += i

if osszeg == szam:
    print('Tökéletes szám!')
else:
    print('Nem tökéletes szám!')