import random
lista = []
n = 20
for i in range (n):
    lista.append(random.randint(100, 1000))

#ezen a ponton adott egy n (20) elemű lista,
#benne 100-999 közötti egész számokkal

#feladat: számoljuk ki a listában szereplő értékek átlagát
#megoldás: Összezés algoritmusának használata

# for - range-el megoldava:

s = 0
for i in range(0, n):
    s += lista[i]
atlag = s / n
print(f'A számok átlaga: {atlag:.2f}')


# print(lista)
# "sima" for-ral
s = 0
for elem in lista:
    #print(elem)
    s += elem
atlag = s / n
print(f'A számok átlaga: {atlag:.2f}')