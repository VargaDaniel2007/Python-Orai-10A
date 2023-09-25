import math

print("Szia én vagyok a pyhton program")

# Kúp felszín, térfogat számítás (kör alapú gúla)

sugar = input("A kúp alapjának sugara: ")
#sugar változó típusa: string
r = float(sugar)

m = float(input("A kúp magassága: "))

s = math.sqrt(r*r + m*m)

A = (r*r * math.pi) + r * s * math.pi

# print("A megadott kúp felszíne:", A)
print(f'A megadott kúp felszíne: {A:.2f}')

V= (r*r * m * math.pi) / 3

print("A kúp térfogata: ", V)