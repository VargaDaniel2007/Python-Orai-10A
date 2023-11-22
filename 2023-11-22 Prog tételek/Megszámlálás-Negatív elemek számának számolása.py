import random

T = []
for i in range (100):
    T.append(random.randint(-100, 100))
print(T)

# Megszámlálás
db = 0
for elem in T:
    if elem < 0:
        db += 1
print(f'A listában {db} db negatív szám van.')