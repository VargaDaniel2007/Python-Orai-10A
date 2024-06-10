from random import randint

def main():
    for i in range(8):
        halmaz = halmaz_feltolto()
        halmaz_e = halmaz_eldonto(halmaz)

        if halmaz_e == False:
            print(f'{i+1}. {halmaz} -> Halmaznak nem tekinthető!')
        else:
            print(f'{i+1}. {halmaz} -> Halmaznak tekinthető!')
    


def halmaz_feltolto():
    halmaz: list[int] = []
    for i in range(5):
        halmaz.append(randint(0, 9))
    return halmaz

def halmaz_eldonto(halmaz):
    stat = dict()

    for sz in halmaz:
        if sz in stat.keys():
            stat[sz] += 1
        else:
            stat[sz] = 1
    
    for k, v in stat.items():
        if v > 1:
            return False
        
    return True

main()