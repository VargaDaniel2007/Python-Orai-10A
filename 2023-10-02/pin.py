#alap + v1
import random, os

def pinRandom():
    pin = ''
    for i in range(0,3):
        pin += str(random.randint(0,9))
        print(pin)
    return pin

def pinBekeres():
    pin = pinRandom()
    mesterkulcs = "123456"
    proba = 3
    while proba > 0:
        pinProba = input('\nKérem a PIN kódot: ')
        if pinProba == pin:
            return True
        elif pinProba == mesterkulcs:
            print(f'A PIN kód: {pin}')
        else:
            proba -= 1
            if proba > 0:
                print(f'HIBÁS, {proba} próbálkozása maradt!')
            else:
                print('\nZÁROLÁS')
    return False
    

def main():
    os.system('cls')
    print("PIN Kód")

    print('\n')
    if pinBekeres() == True:
        print("Sikeres azonosítás")
    
        

main()