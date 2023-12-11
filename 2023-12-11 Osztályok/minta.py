from auto import Auto

audi = Auto()       #Példányosítás
print(type(audi))  # -> <class 'auto.Auto'>
print(audi)        # -> <auto.Auto object at 0x0000018F30D0A950>
audi.rendszam = 'ABC-123'
audi.tipus = 'Audio RS6'
audi.fogyasztas = 14.5
audi.kmOraAllas = 23245
audi.uzemanyagMennyiseg = 23.5
audi.uzemanyagTartalyMeret = 73

print(f'{audi.rendszam}: {audi.tipus}')

vw = Auto()
vw.rendszam = 'DEF-456'
vw.tipus = 'Vw Passat 1.9TDI'
vw.fogyasztas = 7.5
vw.kmOraAllas = 122542
vw.uzemanyagMennyiseg = 3.4
vw.uzemanyagTartalyMeret = 68

autok: list[Auto] = []
autok.append(audi)
autok.append(vw)

for a in autok:
    print(f'{a.rendszam}: {a.tipus}')