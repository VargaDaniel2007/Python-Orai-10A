#Saját megoldás

import random, os

def randomA():
    return random.randint(1, 10)

def randomB():
    return random.randint(1, 10)

def main():
    os.system('cls')
    print('Matematikai műveletek')
    print('\nSzámoljon ki 10 műveletet helyesen')

    pontszam = 0
    muveletSzam = 0
    while pontszam<10:
        muvelet = random.choice(['-', '+', '*'])
        match muvelet:
            case '-':
                a = randomA()
                b = randomB()
                c = a-b
                if int(input(f'{a} - {b} = ')) == c:
                    print('Helyes')
                    pontszam +=1
                else:
                    print(f'Hibás válasz, helyes: {c}')
                muveletSzam += 1
            case '+':
                a = randomA()
                b = randomB()
                c = a+b
                if int(input(f'{a} + {b} = ')) == c:
                    print('Helyes')
                    pontszam +=1
                else:
                    print(f'Hibás válasz, helyes: {c}')
                muveletSzam += 1
            case '*':
                a = randomA()
                b = randomB()
                c = a*b
                if int(input(f'{a} * {b} = ')) == c:
                    print('Helyes')
                    pontszam +=1
                else:
                    print(f'Hibás válasz, helyes: {c}')
                muveletSzam += 1


    print(f'\n{muveletSzam}/{pontszam} = {pontszam/muveletSzam*100:.2f}%')
    input('\nENTER')

main()