import math

def number_input(szoveg: str) -> float:
    szam = 0
    while szam <= 0:
        try:
            szam = float(input(szoveg))
        except:
            pass
    return szam

def teglalap_terulet(tl1, tl2):
    return tl1 * tl2

def haromszog_terulet(hsz1, hsz2, hsz3):
    if (hsz1 + hsz2) > hsz3 and (hsz2 + hsz3) > hsz1 and (hsz3 + hsz1) > hsz2:
        s = (hsz1+hsz2+hsz3)/2
        return math.sqrt(s(s-hsz1)*(s-hsz2)*(s-hsz3))
    else:
        print('A háromszög nem szerkeszthető.')
        return False


#Téglalap oldalai -> terület
#Háromszög oldalai -> terület
#Melyik nagyobb

teglalap1 = number_input('A téglalap első oldala: ')
teglalap2 = number_input('A téglalap második oldala: ')
tgl_t = teglalap_terulet(teglalap1, teglalap2)


haromszog1 = number_input('A háromszög első oldala: ')
haromszog2 = number_input('A háromszög második oldala: ')
haromszog3 = number_input('A háromszög harmadik oldala: ')
hsz_t = haromszog_terulet(haromszog1, haromszog2, haromszog3)

if hsz_t != False and tgl_t > hsz_t:
    print(f'A téglalap területe ({tgl_t}) nagyobb mint a háromszögé ({hsz_t}).')
elif hsz_t != False and tgl_t < hsz_t:
    print(f'A háromszög területe ({hsz_t}) nagyobb mint a téglalapé ({tgl_t}).')
elif hsz_t != False and tgl_t == hsz_t:
    print(f'A négyzet és háromszög területe egyenlő ({hsz_t}).')