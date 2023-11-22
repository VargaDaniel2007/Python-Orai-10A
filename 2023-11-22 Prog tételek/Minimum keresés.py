# Lista deklarálása és feltöltése véletlen számokkal
import random

T = []
for i in range (100):
    T.append(random.randint(-100, 100))
print(T)

minIndex = 0
minErtek = T[0]
for i in range(1, 100):
    if T[i] < minErtek:
        minErtek = T[i]
        minIndex = i

print(f'A legkisebb elem indexe: {minIndex} (sorszáma: {minIndex+1}), értéke {minErtek}')
