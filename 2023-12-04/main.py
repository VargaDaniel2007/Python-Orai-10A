from os import system
from fuggvenyek import ujKorIdo, nyertes

def main():
    menu()

def menu():
    m = '0'
    while m != '6': 
        system('cls')
        print('Időmérő edzés \n\n')
        
        print('1..Új köridő hozzáadása')
        print('2..Leggyorsabb versenyző')
        print('6..Kilépés')
        m = input('\n Menüpont: ')

        match m:
            case '1':
                ujKorIdo()
            case '2':
                nyertes()



    

main()