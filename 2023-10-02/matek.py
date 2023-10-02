from random import randint


def main():
    jovalaszok = 0
    kerdesek = 0
    while jovalaszok < 10:
        kerdesek += 1
        if kerdes():
            jovalaszok += 1
    print(f'A kérdések { (100 * jovalaszok) / kerdesek } %-ra adtál jó választ')

def kerdes() -> bool:
    a = randint(1, 10)
    b = randint(1, 10)
    match randint(1, 3):
        case 1:
            muvelet = '+'
            eredmeny = a + b            
        case 2:
            muvelet = '-'
            eredmeny = a - b            
        case 3:
            muvelet = '*'
            eredmeny = a * b            
    
    tipp = int(input(f'{a} {muvelet} {b} = '))

    return tipp == eredmeny

main()


