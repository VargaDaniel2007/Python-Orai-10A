szam = int(input('Írj be egy pozitív egész számot: '))

prim = True
for i in range(2, szam):
    if szam % i == 0:
        prim = False
        break                   # befejezi a ciklus futását

if prim:
    print('Prím.')
else:
    print('Nem prím.')
