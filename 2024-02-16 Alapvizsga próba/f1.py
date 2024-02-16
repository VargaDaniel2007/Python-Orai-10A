print('1. feladat: Kisebb-nagyobb meghatározása')
a = int(input('Kérem az első számot:'))
b = int(input('Kérem a második számot: '))


if a > b:
    print(f'A nagyobb szám {a}, a kisebb {b}.')
elif b > a:
    print(f'A nagyobb szám {b}, a kisebb {a}.')
else:
    print('A két szám egyenlő')