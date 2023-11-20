#31 elemű list: 2023 májusra vonatkozóan a napi átlaghőmérsékletek
#1 tizedes pontosággal
from random import randint

temperatures = []

def main():
    print('2023 májusi átlaghőmérsékletek\n')
    fillData()
    print(temperatures)
    day = int(input('Melyik nap hőmérsékletére kiváncsi? '))
    print(f'2023 május {day}-n a napi átlaghőmérséklet {temperatures[day-1]} fok volt')

    choice = input('Szeretné az értéket módosítani? (i/N)')
    if choice.lower() == 'i':
        newValue = float(input(f'2023 május {day+1}-ai átlaghőmérséklet: '))
        temperatures[day-1] = newValue
        print(temperatures)

    print(f'Az utolsó májusi napon {temperatures[-1]} fok volt az átlag hőmérséklet')

    print('Az első hét hőmérséklet adatai:')
    for i in range(0, 7):
        print(temperatures[i], end='  ')
    print('\n')
    print('Második hét adatai: ',temperatures[7:14]) #Vége nem számít


def fillData():
    mode = ''
    while mode.upper() != 'K' and mode.upper() != 'V':
        mode = input('Adatfelviteli módja ([K]ézzel / [V]életlen Számokkal): ')
    if mode == 'K':
        fillByUser()
    else:
        fillWithRandomNumbers()

def fillByUser():
    for i in range(31):
        temp = float(input(f'2023 május {i+1}-ai átlaghőmérséklet: '))
        temperatures.append(temp)

def fillWithRandomNumbers():
    for i in range(31):
        temp = randint(-20, 330) / 10   #-2 - 33
        temperatures.append(temp)
#HF Ne legyenek nagy kilengések (+-5 fok)

main()