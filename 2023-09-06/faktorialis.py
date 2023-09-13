# 5! = 1 * 2 * 3 * 4 * 5

n= int(input("Kérem a számot: "))
fakt = 1
# for i in range(n):
#     fakt = fakt * (i + 1) 

for i in range(1, n + 1):
    fakt *= i

print(f'{n}! = {fakt}')