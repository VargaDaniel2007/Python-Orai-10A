felhasznalo_nev = "bori99"
jelszo = "Szivecske<3"

bekert_felh_nev = ''
bekert_jelszo = ''

while felhasznalo_nev != bekert_felh_nev or jelszo != bekert_jelszo:
    bekert_felh_nev = input('Adja meg a felhasználónevét! ')
    bekert_jelszo = input('Adja meg a jelszavát! ')

    if felhasznalo_nev != bekert_felh_nev or jelszo != bekert_jelszo:
        print('Belépés megtagadva.')


print('Belépés engedélyezve.')
