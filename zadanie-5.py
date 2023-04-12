def liczby_drugie_hehe():
    liczba = 1
    while True:
        licznik = 0
        for x in range (liczba//2):
            if x == 0 or x == 1 or liczba % x == 0:
                licznik += 1
                print("not prime")
        if licznik == 0:
            yield liczba
            print("prime")
        liczba += 1

generator = liczby_drugie_hehe()
for x in range (20):
    print(next (generator))