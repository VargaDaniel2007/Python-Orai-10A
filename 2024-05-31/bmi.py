tomeg = float(input('Kérem a test tömeget (kg): '))
magassag = float(input('Kérem a magasságot (m): '))

bmi = tomeg / (magassag * magassag)

print(f'A testtömeg indexed: {bmi:.2f}')
if bmi < 20:
    print('Sovány vagy.')
elif 20 <= bmi <= 25:
    print('Normális a testalkatod!')
else:
    print('Túlsúlyos vagy.')