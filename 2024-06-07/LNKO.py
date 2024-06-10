print('LNKO kivonásos algoritmussal')

a = int(input('a = '))
b = int(input('b = '))

eredeti_a = a
eredeti_b = b

while a != b:
    if a > b:
        a = a-b
    elif b > a:
        b = b-a
        
        
print(f'LNKO({eredeti_a},{eredeti_b}) = {a}')
