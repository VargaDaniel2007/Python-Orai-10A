def szokoev_e(ev:int) -> bool:
    if ev % 400 == 0:
        return True
    if ev % 100 == 0:
        return False
    return ev % 4 == 0

print('2. feladat: Szökőév listázó')
a = int(input('Kérem az egyik évszámot:'))
b = int(input('Kérem a másik évszámot: '))

if a > b:
    evtol = b
    evig = a
else:
    evtol = a
    evig = b

szokoevek: list[int] = []
for ev in range(evtol, evig+1):
    if szokoev_e(ev):
        szokoevek.append(ev)

if len(szokoevek) == 0:
    print('Nincs szökőév a megadott tartományban!')
else:
    print('Szokőévek: ', end='')
    for ev in szokoevek:
        if ev == szokoevek[-1]:
            print(ev)
        else:
            print(f'{ev}; ', end='')
    