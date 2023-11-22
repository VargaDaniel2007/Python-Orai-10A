# 20 elemű lista feltöltése, és annak eldöntése, hogy
# van-e az elemek között negatív érték (F feltétel)

import random

T = []
for i in range (20):
    T.append(random.randint(-2, 100))
print(T)

#eldöntés
i = 0
while i < 20 and T[i] >= 0:
    i += 1
if i < 20:
    print('A listában van negatív szám')
else:
    print('A listában nincs negatív szám')


# Ugyanez egy másik algoritmussal de csak Python-ban (NEM EZT KELL TUDNI)
for elem in T:
    if elem < 0:
        print('A listában van negatív szám')
        break
else:
    print('A listában nincs negatív szám')