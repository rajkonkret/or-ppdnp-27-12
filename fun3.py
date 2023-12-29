# zmienne o zasięgu globalnym
a = 10
b = 10


def dodaj():
    a = 6  # a i b są o zasięgu lokalnym dla tej funkcji
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)  # użyje zmiennych globalnych


def dodaj3():
    global a  # a globalne zostanie nadpisane wewnątrz funkcji
    a = 6  # to a jest globalne
    b = 7
    print(a + b)


print(f"Zmienna a z góry {a}")  # Zmienna a z góry 10
dodaj()  # 13
print(f"Zmienna a z góry {a}")  # Zmienna a z góry 10
dodaj2()  # 20
print(f"Zmienna a z góry {a}")  # Zmienna a z góry 10
dodaj3()  # 13
print(f"Zmienna a z góry {a}")  # Zmienna a z góry 6
dodaj2()  # 16
