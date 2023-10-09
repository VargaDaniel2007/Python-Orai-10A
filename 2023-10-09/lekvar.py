#Saját megoldás

import random

osszesTermes = 0
legkisebbTermes = 11
legkevesebbNap = ''
for i in range(1, 31):
    napi = random.randint(0, 10)
    
    print(f'{i}. {napi} kg')
    osszesTermes += napi
    
    if legkisebbTermes >= napi:
        legkisebbTermes = napi
        legkevesebbNap += str(i) + '. '

print(f'Mari néni {osszesTermes} kg epret szedett.')

if legkisebbTermes == 0:
    print(f'{legkevesebbNap} napo(ko)n nem szedett termést')
else:
    print(f'Mari néni a {legkevesebbNap} napo(ko)n {legkisebbTermes} kg epret szedett')

eperAr = osszesTermes * 450
lekvarAr = (2 * osszesTermes) * 600
print(f'Mari néni haszna: {lekvarAr - eperAr} Ft')

palinkaFelLiter = (osszesTermes / 4) 
palinkaAr = (palinkaFelLiter/2) * 4000
print(f'Ha Pista bácsi uralta volna az epret akkor {palinkaAr - eperAr} Ft haszna lett volna')