import os

os.system('cls')

def main():
    print("Hányszor látták a medvét")
    print('\nKérem írja be a hét nap reggeli, déli és esti mérését (Egész vagy tizedes szám): \n')

    napok = ''
    for i in range(0, 7):
        x = 0
        print(f'{i+1}. Nap')
        x =+ float(input(f'Regggel: '))
        x =+ float(input(f'Délben: '))
        x =+ float(input(f'Este: '))
        print('\n')
        
        atlx = x/3
        if atlx > 10:
            napok += str(i+1) + '. '
    if napok == '':
        print('A gyerekek egyik napon se látták a medvét.')
    else:
        print(f'A gyerekek a {napok}napokon látták a medvét.')
        





main()