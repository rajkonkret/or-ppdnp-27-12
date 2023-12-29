# funkcje zwracające wynik
# return - zwróc wynik

def dodaj(a, b):
    return a + b


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(5, 6))
print(dodaj(5, 6) + dodaj(1, 2))  # 14
a = dodaj(5, 6)
print("Wynik działania", a)  # Wynik działania 11

print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))
print(oblicz_vat(cena=2000))
print(oblicz_vat(cena=2000, vat=8))
print(oblicz_vat(vat=8, cena=3000))
# 1230.0
# 1070.0
# 2460.0
# 2160.0
# 3240.0

zm = oblicz_vat(1000)  # 1230.0
if zm == 1230:
    print("Ok")  # Ok
