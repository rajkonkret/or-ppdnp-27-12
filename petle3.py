dictionary = {'imie': 'Radek', "nazwisko": "Kowalski"}

# wypisze klucze
for k in dictionary:
    print(k)  # nazwisko

for k in dictionary.keys():
    print(k)  # nazwisko

# wypisze wartości
for v in dictionary.values():
    print(v)  # Kowalski

# wypisanie par
for i in dictionary.items():
    print(i)  # ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)  # imie => Radek
