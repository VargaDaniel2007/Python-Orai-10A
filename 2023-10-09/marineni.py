import random

minSzedes = 11
minSzedesNapok = ''
osszes = 0

for i in range(1,31):
    szedes = random.randint(0, 10)
    osszes += szedes

    if szedes < minSzedes:
        minSzedes = szedes
        minSzedesNapok = str(i)
    elif szedes == minSzedes:
        minSzedesNapok+= ', ' + str(i)

    print(f'{i}. {szedes} kg')

print(f'Mari néni a hónap során {osszes} kg epret szedett')    
if minSzedes == 0:
    print(f'Mari néni a {minSzedesNapok} napokon nem szedett epret')
else:
    print(f'Mari néni a {minSzedesNapok} napokon szedte a legkevesebbet: {minSzedes} kg')

print(f'Mari néni a lekvár bizniszből {(1200-450) * osszes} Ft hasznot termelt')

print(f'Pista bácsi ebből az eperből főzött volna {osszes/8} l pálinkát, ez a biznisz {4000*(osszes/8) - 450*osszes} Ft hasznot hozott volna')
