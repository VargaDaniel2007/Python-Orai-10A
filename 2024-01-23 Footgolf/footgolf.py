from versenyzo import Versenyzo

versenyzok: list[Versenyzo] = []

f = open('fob2016.txt', 'r')
for sor in f:
    versenyzok.append(Versenyzo(sor))    
f.close()

print(f'3. feladat: Versenyzők száma: {len(versenyzok)}')

nok = 0
for v in versenyzok:
    if v.kategoria == 'Noi':
        nok += 1
print(f'4. feladat: A női versenyzők aránya: { (nok / len(versenyzok)) * 100:.2f} %')

