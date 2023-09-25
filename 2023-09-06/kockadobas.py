import random
'''
dobas1 = random.randint(1, 6)
dobas2 = random.randint(1, 6)
dobas3 = random.randint(1, 6)
dobas4 = random.randint(1, 6)
dobas5 = random.randint(1, 6)
dobas6 = random.randint(1, 6)

print("A 6 dobás összege", dobas1 + dobas2 + dobas3 + dobas4 + dobas5 + dobas6)
'''


osszeg = 0
for i in range(7, 1, -1):
    print(i)
    dobas = random.randint(1, 6)
    osszeg += dobas #osszeg = osszeg + dobas

print(f'A dobás összege: {osszeg}')