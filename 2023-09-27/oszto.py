szam = int(input('Írj be egy pozitív egész számot:'))
print(f'{szam} osztói: ', end='')

for i in range(1, szam + 1):
    if szam % i == 0:
        if szam == i:
            print(i)
        else:
            print(i, end="; ")

