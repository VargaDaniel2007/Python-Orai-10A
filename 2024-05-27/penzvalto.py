arfolyam = 365

valtas = input('Eurót (EUR) vagy forintot (HUF) akarsz váltani? ')

if valtas.upper() == 'EUR':
    euro = int(input('Hány eurót akarsz beváltani? '))
    print(f'{euro} euróért {euro*arfolyam} forintot kapsz.')
else:
    forint = int(input('Hány forintot akarsz beváltani? '))
    print(f'{forint} forintért {forint/arfolyam:.2f} eurót kapsz.')