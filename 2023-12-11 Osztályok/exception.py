def szamBekeres() -> int:
    x = None
    while x == None:
        try:
            x = int(input('Kérem a számot: '))
        except:
            x = None
    return x
print(f'A bekért szám: {szamBekeres()}')