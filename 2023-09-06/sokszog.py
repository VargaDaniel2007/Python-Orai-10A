#Sokszög kerülete

oldszam = int(input("Sokszög oldalainak száma: "))
osszhossz = 0
if oldszam > 3:
    for i in range(oldszam):
        oldhossz = int(input(f'Kérem az {i+1}. oldal hosszát: '))
        osszhossz += oldhossz
    print(f'A sokszög kerülete: {osszhossz}')
else:
    print("Nincs ilyen sokszög.")
