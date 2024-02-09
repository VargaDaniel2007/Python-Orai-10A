# Dictionary

szotar = dict()

#elem(ek) hozzáadása
szotar['alma'] = 'apple'       #key: 'alma', value: 'apple'
szotar['barack'] = 'appricot'  #key: 'barack', value: 'appricot'

#elemek kiírása a képernyőre
print(szotar)               #eredmény: {'alma': 'apple', 'barack': 'peach'}

#elemek képernyőre írása ciklussal:
for key, value in szotar.items():
    print(f'{key} - {value}')


#elem értékének módosítása -> egy adott kulcshoz tartozó érték módosítása
# (kulcs nem módosítható)
szotar['barack'] = 'peach'
print(szotar)

#elem törlése -> adott kulcs törlése
del szotar['barack']
print(szotar)

# Ellenőrzés: létezik-e a kulcs a szótárban
if 'alma' in szotar.keys():
    print('Az alma benne van a szótárban')
else:
    print('Az alma nincs benne a szótárban')
    
if 'barack' in szotar.keys():
    print('Az barack benne van a szótárban')
else:
    print('Az barack nincs benne a szótárban')