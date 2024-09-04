from random import randint

def main():
    szamok: list[int]= []

    for i in range(10):
        szamok.append(randint(10,99))

    print(szamok)
    if ez_prim(szamok):
        print('Van prímszám a listában!')
    else:
        print('Nincs prímszám a listában!')
    
            
    
def ez_prim(szamok: int):
    for sz in szamok:
        i = 3
        while i != sz and sz % i != 0:
            i += 1
        if i == sz:
            return True
    


main()