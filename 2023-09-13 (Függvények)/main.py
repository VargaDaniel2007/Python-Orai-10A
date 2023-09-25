#Függvények
#Függvény elnevezés kategóriák
# - "snake case":   pl.: veletlen_szam_generalas
# - "pascal case":  pl.: VeletlenSzamGeneralas
# - "camel case":   pl.: veletlenSzamGeneralas

import random

#Függvény fela1data: 1 számot "húz" a 90-ből
def szamHuzas1Tol9Ig() -> int:      #visszatérési érték megadása nem kötelező
    szam = random.randint(1, 90)
    return szam

# szamhúzás, univerzálisabb (5/90, 6/45, 7/35)
def szamHuzas(maxÉrték: int):   #Paraméter típusának megadása nem kötelező
    szam = random.randint(1, maxÉrték)
    return szam

#Összeadás függvény: osszeadas -> két valós számot ad össze
#visszatérési értéke szintén valós
def osszeadas(szam1: float, szam2: float) -> float:
    eredm = szam1 + szam2
    return eredm

def kerekites(a: float) -> int:
    kerekitett = int(a + 0.5)
    return kerekitett

def alapMuvelet(a, muvelet, b):      #Nem használok típusokat
    match muvelet:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case _:                     #Else ág -> ha egyik korábbinak se felelt meg
            return None

def egeszSzamBekeres(szoveg: str,) -> int:
    s = ''
    while not s.isdecimal():
        s = input(szoveg)
    return int(s)

#egész számot kér be, egy megadott tartományból (pl.: 1-999)
#1. megoldas
def egeszSzamBekeres2(szoveg: str, min: int, max: int) -> int:
    szam = min - 1
    while not szam < min or szam > max:
        szam = egeszSzamBekeres2(szoveg)
    return szam

#2. megoldas
def egeszSzamBekeres3(szoveg: str, min: int, max: int) -> int:
    s=''
    while not s.isdecimal() or (int(s) < min or int(s) > max):
        s = input(szoveg)
    return int(s)
    

# x = szamHuzas1Tol9Ig()
# print(x)

# y = szamHuzas(45)
# print(y)

# print(osszeadas(12, 34))

# print(alapMuvelet(2, "+", 4))
# print(alapMuvelet(2, "*", 6))
# print(alapMuvelet(4, "/", 1))
# print(alapMuvelet(6, "-", 1))

f = egeszSzamBekeres("Kérem a számot: ")
print(f)

honap = egeszSzamBekeres2('Kérem adja meg a hónap sorszámát: ', 1, 12)
print(honap)

honap2 = egeszSzamBekeres3('Kérem adja meg a hónap sorszámát: ', 1, 12)
print(honap2)