pizza_ar = 4990
cola_ar = 499

egyenleg = int(20000)

#Mennyi pizza mennyi üdítő, van pénze vagy nincs, ha igen mennyibe kerül, mennyi marad
#----------------------------
pizza_db = int(input("Mennyi pizzát kér: "))
cola_db = int(input("Mennyi Colát kér: "))

pizza_ossz = int(pizza_ar * pizza_db)
cola_ossz = int(cola_ar * cola_db)
if pizza_ossz + cola_ossz > egyenleg:
    print("Nem tudjuk teljesíteni a rendelését.")
else:
    print(f'A rendelés {pizza_ossz + cola_ossz}-be kerül, {egyenleg - pizza_ossz + cola_ossz} pénze maradt')