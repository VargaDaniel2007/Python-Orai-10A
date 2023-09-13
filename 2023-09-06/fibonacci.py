#Feladat: kérjen be a felhasználótól egy egész számot és írja ki a megadott
# sorszámú elemét a fibonacci sorozatnak
#Pl.: 5-> (1 1 2 3) 5
#Pl.: 10 -> (1 1 2 3 5 8 13 21 34) 55

n = int(input("Hányadik elemét szeretné tudni a Fibonacci sorozatnak? "))
if n < 0:
    print("Ilyen sorszámú elem nincs.")
elif n == 0:
    print(f'A Fibonacci sorozat {n}. eleme: 0')
elif n <= 2:
    print(f'A Fibonacci sorozat {n}. eleme: 1')
else:
    a = 1
    b = 1
    for i in range(n - 2):
        c = a + b
    
        a = b
        b = c

    print(f'A Fibonacci sorozat {n}. eleme: {b}')