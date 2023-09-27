
def main():
    maxPrim = int(input('Prímszám keresésének felső határa: '))
    print('Ezeket a prímszámokat találtam: ')
    for i in range(2, maxPrim + 1):
        if prim_e(i):
            print(i, end='; ')

def prim_e(szam: int) -> bool:
    for i in range(2, szam):
        if szam % i == 0:
            return False

    
    return True

main()