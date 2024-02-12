from uzenet import Uzenet

uzenetek: list[Uzenet] = []

def main():
    beolvasas()
    utolso_uzenet_a_telefonban()
    leghosszabb_es_legrovidebb_uzenet()

def beolvasas() -> int:
    f = open('sms.txt', 'r', encoding='utf-8')
    uzenetek_szam = int(f.readline())
    for i in range(uzenetek_szam):
        sor1 = f.readline()
        sor2 = f.readline()
        uzenetek.append(Uzenet(sor1, sor2))
    f.close()

    return uzenetek_szam

def utolso_uzenet_a_telefonban():
    print('2. feladat')
    if len(uzenetek) > 10:
        uzenet = uzenetek[9]
    else:
        uzenet = uzenetek[-1]
    print_uzenet(uzenet)

def leghosszabb_es_legrovidebb_uzenet():
    leghosszabb_uzenet = uzenetek[0]
    legrovidebb_uzenet = uzenetek[0]
    for u in uzenetek[1:]:
        if len(u.uzenet) > len(leghosszabb_uzenet.uzenet):
            leghosszabb_uzenet = u
        if len(u.uzenet) < len(legrovidebb_uzenet.uzenet):
            legrovidebb_uzenet = u
    
    print('3. feladat:')
    print('\tLeghosszabb üzenet:')
    print_uzenet(leghosszabb_uzenet)
    print('\tLegrövidebb üzenet:')
    print_uzenet(legrovidebb_uzenet)


def print_uzenet(uzenet: Uzenet):
    print(f'\t{uzenet.ora}:{uzenet.perc} {uzenet.telefonszam}')
    print(f'\t{uzenet.uzenet}')

main()