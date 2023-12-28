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

dict2 = {'name': 'imie', 'company': 'Orange'}
print(type(dict2))
print(dict2)  # {'name': 'imie', 'company': 'Orange'}
# zamiana w słowniku kluczy z wartościami
print({value: key for key, value in dict2.items()})  # {'imie': 'name', 'Orange': 'company'}
d2 = {}
for key, value in dict2.items():
    d2[value] = key

print(d2)  # {'imie': 'name', 'Orange': 'company'}
