# petla - wielokrotnie wykonuje blok kodu
# for  - petla iteracyjna
import random

for i in range(10):  # 0..9
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # _ niema zmienna
    pass

for i in range(10):
    print(i * 2)

print("----------")
# Przerobic boiler kod z zadania random na petle for
lista_lotto = list(range(1, 50))  # 1..49
for i in range(6):  # 0..5
    wyn = random.choice(lista_lotto)  # zapisanie wylosowanej do zmiennej
    lista_lotto.remove(wyn)  # usunięcie wylosowanej z listy (z bębna losującego)
    print(wyn, end=' ')  # wydrukowanie wylosowanej liczby
# ----------
# 31 17 40 35 8 13
print()  # dodanie pustej lini, znak konca lini ustawiony na \n
print("Dalsza część programu")

for i in range(10):
    if i % 2 == 0:
        print(i, "liczba parzysta")
# Dalsza część programu
# 0 liczba parzysta
# 2 liczba parzysta
# 4 liczba parzysta
# 6 liczba parzysta
# 8 liczba parzysta

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

lista4 = []
for j in range(10):
    if j % 2 == 0:
        lista4.append(j)

print(lista4)  # [0, 2, 4, 6, 8]

for c in lista4:
    if c == 2:
        c += 1  # c = c + 1
    print(c)  # 2 -> 3

a = 1
a += 1  # a = a + 1
print(a)  # 2
a -= 1  # a = a - 1
print(a)  # 1
a *= 3  # a = a * 1
print(a)  # 3
a /= 1  # a = a / 1
print(a)  # 3.0
a %= 2  # a = a % 1
print(a)  # 1.0

imiona = ['Radek', 'Asia', 'Zbyszek', 'Robert']
for p in imiona:
    print(p)
# Radek
# Asia
# Zbyszek
# Robert

# wypisac z listy imiona wraz z indeksem
# 0 Radek

# index()
for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Robert
# range(3) 0..2, len(imiona) - 4, range(len(imiona)) , range(4) - 0..3
for p in range(len(imiona)):
    print(p, imiona[p])  # p to numer indeksu
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Robert

# enumerate() - zwraca element kolekcji wraz numerem indeksu
for p in enumerate(imiona):
    print(p)  # (3, 'Robert')

a, b = (3, 'Robert')
print(a, b)

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Robert
for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Asia
# 3 Zbyszek
# 4 Robert

ludzie = ["Radek", 'Zenek', 'Asia', 'Marcin', 'Robert', "Tomek"]
wiek = [47, 67, 34, 32, 40]
# wypisac indeks, osobe i wiek
# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])
#     # dla różnych długości list dostaniemy bład:
#     # IndexError: list index out of range
# 0 Radek 47
# 1 Zenek 67
# 2 Asia 34
# 3 Marcin 32
# 4 Robert 40

# zip() - łączy kolekcje w jedna
for k in zip(ludzie, wiek):
    print(k)  # ('Robert', 40)

for o, w in zip(ludzie, wiek):
    print(o, w)
# Radek 47
# Zenek 67
# Asia 34
# Marcin 32
# Robert 40
for p in enumerate(zip(ludzie, wiek)):
    print(p)  # (4, ('Robert', 40))

a, b = (4, ('Robert', 40))
print(a, b)  # 4 ('Robert', 40)
c, d = b
print(c, d)  # Robert 40
a, (c, d) = (4, ('Robert', 40))
print(a, c, d)  # 4 Robert 40
for i, (o, w) in enumerate(zip(ludzie, wiek)):
    print(i, o, w)
# 0 Radek 47
# 1 Zenek 67
# 2 Asia 34
# 3 Marcin 32
# 4 Robert 40
# zip_longest
for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(-10, 0, 2):
    print(i)

for i in range(0, -10, -1):  # krok ujemny, pętla odlicza w tył
    print(i)

for i in range(10, 1, -2):
    print(i)
