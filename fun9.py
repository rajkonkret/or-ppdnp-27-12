# funkcja lambda
# skrócony zapis funkcji
# mozliwosc deklaracji w miejscu wykonania

def odejmij2(a, b):
    return a - b


print(odejmij2(2, 3))

odejmij = lambda a, b: a - b  # lambda ma return automatycznie
print(odejmij(5, 6))  # -1

oblicz_vat = lambda cena, vat=23: cena * (vat + 100) / 100
print(oblicz_vat(1000))  # 1230.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(1))
print(wiek(10))
print(wiek(18))

lista = [1, 2, 3, 4, 10, 20, 50]
for i in lista:
    print(i * 2)

print([i * 2 for i in lista])


def zmien(x):
    return x * 2


# map() - mapuje(modyfikuje) kolejne elemnty kolekcji (taki for)
print(f'Zastosowanie map {list(map(zmien, lista))}')  # Zastosowanie map [2, 4, 6, 8, 20, 40, 100]
print(f'Zastosowanie map {list(map(lambda x: x * 2, lista))}')  # Zastosowanie map [2, 4, 6, 8, 20, 40, 100]
# lambda jako funkcja anonimowa

# filter() - zwraca pasujące do wzorca elementy (to taki for z ifem)
# wzorzec przekazany za pomoca funkcji
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter(): [1, 2]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 8, lista))}")
# Zastosowanie filter(): [10, 20, 50]
print(f"Zastosowanie filter(): {list(filter(lambda x: x % 2 == 0, lista))}")
# Zastosowanie filter(): [2, 4, 10, 20, 50]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 20, lista))}")
# Zastosowanie filter(): [4, 10]
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 20, lista))}")
# Zastosowanie filter(): [4, 10]
