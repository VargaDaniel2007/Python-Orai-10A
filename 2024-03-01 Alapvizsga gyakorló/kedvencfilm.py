from filmalap import oraperc

for i in range(0, 3):
    film_nev = input('Add meg egy film címét! ')
    idotartam = int(input('Hány perces a film? '))
    print(f'A(z) {film_nev} című film {oraperc(idotartam)} hosszú.')