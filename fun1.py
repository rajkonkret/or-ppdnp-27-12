# funkcje/metody - wydzielony fragment kodu, który można wykonać w dowolnej chwili
# funkcja ma definicje - w tym miejscu nie jest wykonywana
# funkcja ma miejsce wywołania czyli wykonania

a = 1
b = 5


# definicja funkcji - tu sie funkcja nie wykonuje
def dodaj():
    print(a + b)


def dodaj2(a, b):  # dwa argumenty obowiązkowe
    print(a + b)  # uzyje a i b z argumentów(ma lokalne)


def odejmij(a, b, c=0):  # c ma wartość domyślną
    print(a - b - c)


# wywołąnie funkcji - nazwa funkcji i nawiasy okrągłe
dodaj()  # 6
dodaj2(4, 5)  # 9
odejmij(1, 2)  # -1 c=0
odejmij(1, 2, 3)  # -4 c=3
odejmij(b=7, a=9, c=8)  # -6 argumenty po nazwie

# print(odejmij(1, 2) + dodaj())  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
print(dodaj())  # None
