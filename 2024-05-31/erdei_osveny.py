from random import randint
# 0 -> szárazföld, 1 -> pocsolya

def main():
    osveny: list[int] = []

    for i in range(25):
        osveny.append(randint(0, 1))

    nem_kel_at = atkeles(osveny)

    print(osveny)
    if nem_kel_at == True:
        print('Piroska nem tud átkelni száraz lábbal az ösvényen.')
    else:
        print('Piroska át tud átkelni száraz lábbal az ösvényen.')

def atkeles(osveny):
    pocsolyak = 0
    for p in osveny:
        if pocsolyak == 4:
            return True
        elif p == 1:
            pocsolyak += 1
        else:
            pocsolyak = 0
    return False




main()