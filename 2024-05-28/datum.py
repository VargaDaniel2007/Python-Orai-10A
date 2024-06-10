max_napok = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def number_input(szoveg: str, max: int) -> int:
    szam = 0
    while szam <= 0 or szam > max:
        try:
            szam = int(input(szoveg))
        except:
            pass
    return szam

def datum_kulonbseg(ev1, ho1, nap1, ev2, ho2, nap2):
    napok1 = ev1*365
    for i in range(0, ho1):
        napok1 += max_napok[i]
    napok1 += nap1

    napok2 = ev2*365
    for i in range(0, ho2):
        napok2 += max_napok[i]
    napok2 += nap2

    return abs(napok1-napok2)



datum_ev  = number_input('Kérem az első dátum évét: ', 2030)
datum_honap = number_input('Kérem az első dátum hónapját: ', 12)
datum_nap = number_input('Kérem az első dátum napját: ', max_napok[datum_honap-1])

datum_ev2  = number_input('Kérem a második dátum évét: ', 2030)
datum_honap2 = number_input('Kérem a második dátum hónapját: ', 12)
datum_nap2 = number_input('Kérem a második dátum napját: ', max_napok[datum_honap2-1])

print(f'{datum_ev}. {datum_honap}. {datum_nap}. és {datum_ev2}. {datum_honap2}. {datum_nap2}. között {datum_kulonbseg(datum_ev, datum_honap, datum_nap, datum_ev2, datum_honap2, datum_nap2)} nap telt el.')