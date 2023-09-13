ma_ev = 2023
ma_ho = 9
ma_nap = 4

#------------

szul_ev = int(input("Születési év: "))
if ma_ev-18 > szul_ev:
    print("Vehet piát!")
elif ma_ev-18 < szul_ev:
    print("Majd legközelebb, előbb nőlj nagyra...")
else:
    szul_ho = int(input("Születési hónap: "))
    if szul_ho < ma_ho:
        print("Tessék itt, a fröccs...")
    elif szul_ho > ma_ho:
        print("Majd legközelebb, előbb nőlj nagyra...")
    else:
        szul_nap = int(input("Születési nap: "))
        if szul_nap < ma_nap:
            print("Tessék itt, a fröccs...")
        elif szul_nap > ma_nap:
            print(f'Gyere vissza {szul_nap - ma_nap} nap múlva.')
        else:
            print("18. szülinapod alkalmából az első ital ingyen van.")    
    

