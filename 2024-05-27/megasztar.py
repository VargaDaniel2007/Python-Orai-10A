import random

def main():
    pontszamok = []
    for i in range(0, 5):
        pontszamok.append(random.randint(1, 10))
    
    ossz = osszpontszam(pontszamok)

    print(f'{pontszamok} -> összpontszám: {ossz} pont')

def osszpontszam(pontok):
    maxertek =  pontok[0]
    ossz = 0

    for p in pontok:
        ossz += p
        if p > maxertek:
            maxertek = p
    
    return ossz-maxertek



main()