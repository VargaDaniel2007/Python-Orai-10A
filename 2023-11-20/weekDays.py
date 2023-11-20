weekDays = ['hétfő', 'kedd', 'zserda', 'csütörtök', 'péntek', 'szombat', 'vasárnap']
emptyList = []

def main():
    print(weekDays)
    print(f'A hét ötödik napja {weekDays[4]}')
    #lista elem értékének módosítása:
    weekDays[2] = 'szerda'
    print(weekDays)

    n = weekDays.index('kedd')
    print(f'A(z) első "kedd" értékű elem indexe a listában: {n}')


main()

