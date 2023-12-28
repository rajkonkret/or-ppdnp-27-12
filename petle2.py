# while - petla sterowana warunkiem
# dopóki warunek True pętla się wykonuje

licznik = 0
while True:
    licznik += 1
    print("komunikat!")
    if licznik > 10:
        break  # przerywa działanie pętli

print(licznik)  # 11

licznik = 0
while licznik < 11:
    print("Komunikat!!")
    licznik += 1

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)
print(lista_int)
# ['3', '4', '2', '77', '88', '23124'] -> str
# [3, 4, 2, 77, 88, 23124] -> int
