from random import randint


def main():
    penz = 1000
    tovabb = 'i'
    print(f'Az ön egyenlege: {penz} krajcár')
    while tovabb == 'i':
        t = tet(penz)
        v = tipp()
        dobas = randint(1, 6)
        print(f'Dobás {dobas},', end=' ')
        if (v == 'a' and dobas <= 2) or (v == 'b' and dobas >= 3 and dobas <= 4) or (v == 'c' and dobas >= 5):
            print('Ön nyert')
            penz += t* 2
        else:
            print('Ön vesztett')
            penz -= t
       
        print(f'Az ön egyenlege: {penz} krajcár')

        if penz > 0:
            tovabb = input('Folytatja (i/n): ')



def tipp() -> str:
    v = ''
    while v != 'a' and v != 'b' and v != 'c':
        print('\ta: 1-es vagy 2-es')
        print('\tb: 3-es vagy 4-es')
        print('\tc: 5-es vagy 6-es')
    
        v = input('Választás: ')
    return v

def tet(penz: int) -> int:
    t = 0
    while t <= 0 or t > penz:
        t = int(input('Mekkora összeget kockáztat? '))
    return t

main()