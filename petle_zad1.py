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
