import random

def main():
    print("Pista bácsi pálinkát főz...")

    keszlet = 0
    masnapos = False
    napok = ''
    maxKeszlet = 0
    maxNap= 0
    for i in range(0, 30):
        print(f'{i+1}. nap')
        if not masnapos:
            fozes = random.randint(1,5)
            print(f'     Főzés: {fozes} l')
            keszlet += fozes
            if fozes == 5:
                napok += str(i + 1) + ' '
            if random.randint(1, 100) >= 80:        #buli volt...
                keszlet -= 1
                masnapos = True
                print('     buli van')
        else: 
            masnapos = False
            print('     Szünnap')
        print(f'     Készlet: {keszlet} l')
        if keszlet > maxKeszlet:
            maxKeszlet = keszlet
            maxNap = i+1

    print('------------------------------')
    print(f'A maximális készlet {maxKeszlet} l volt, a {maxNap}. napon')
    print(f'Pista bácsi a {napok} napokon főzőtt 5l kisüstit.')



main()
