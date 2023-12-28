# słownik - typdanych w rodzaju para klucz wartosc
# json {"name":"Radek"} para {klucz:wartość}
# { "klucz" :  "wartość" }
# klucze muszą byc unikalne

dictionary = {}  # pusty słownik
print(dictionary)  # {}

# dodawanie elemntu do słownika
dictionary['imie'] = 'Radek'
print(dictionary)  # {'imie': 'Radek'}
print(type(dictionary))  # <class 'dict'>

print(dictionary.values())  # dict_values(['Radek'])
print(dictionary.keys())  # dict_keys(['imie'])
print(dictionary.items())  # dict_items([('imie', 'Radek')])

dictionary.update({"date": "31-12-2023"})
print(dictionary)  # {'imie': 'Radek', 'date': '31-12-2023'}

dictionary1 = {'x': 2}
dictionary1.update([('y', 2), ('z', 0)])  # dodanie wielu par jako listy krotek
print(dictionary1)  # {'x': 2, 'y': 2, 'z': 0}

# słownik polsko angielski
dict2 = {'imie': 'name', 'kot': 'cat'}
print(dict2['imie'])  # name

# wypisac słowa, które umiemy przetłumaczyc
# pobrac od uzytkownika słowko do przetłumaczenia
# wypisać tłumaczenie
print("Mam w słowniku", dict2.keys())
key = input("Podaj słowo do przetłumaczenia")  # input zwraca str
print(f"Tłumaczenie słowa {key} to {dict2[key.replace(" ", "").lower()]}")

# kalkulator
# pobrac dwie liczby
# wypisac wynik obliczenia np." 1 + 2 = 3
# input zwraca str
# przy obliczeniach zamieniamy str na liczby np.: float, int
a = input("Podaj pierwszą liczbe")
b = int(input("Podaj druga liczbe"))
print(float(a) + b)
