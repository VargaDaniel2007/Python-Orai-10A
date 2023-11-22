# Lista deklarálása és feltöltése véletlen számokkal
import random

T = []
for i in range (100):
    T.append(random.randint(-100, 100))
print(T)

ertek = int(input('Keresett érték: '))

i = 0
while i < len(T) and T[i] != ertek:
    i += 1
if i < len(T):
    print(f'A listában a {i+1}. elem a keresett érték')
else:
    print('A listában nem szerepel a keresett érték')