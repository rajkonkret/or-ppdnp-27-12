# lista - przechowuje elemnty różnego typu w jednej liscie
# zachowuje kolejnosć przy dodawaniu elemnentów

# definicja pustej listy
lista = []  # pusta lista
print(lista)  # []
print(type(lista))  # <class 'list'>

print(bool(lista))  # False

# dodawanie elemntów do listy
lista.append("Radek")
lista.append("Maciek")
lista.append("MArek")
print(lista)  # ['Radek', 'Maciek', 'MArek']
lista.append("Marta")
lista.append("Zenek")
lista.append("Jaśko")
lista.append("Radek")
print(lista)  # ['Radek', 'Maciek', 'MArek', 'Marta', 'Zenek', 'Jaśko', 'Radek']
# lista jest indeksowana od 0
# wypisanie z listy po indeksie
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])  # Marta

# print(lista[10])  # IndexError: list index out of range
print(len(lista))  # długosc listy = 7, ale ostatni indeks 6 bo indeksujemy od 0
print(lista[-1])  # Radek, ostatni element
print(lista[-2])
print(lista[-3])
print(lista[-4])
lista.append("Adam")
print(lista[-0])  # Radek pierwszy element

print(lista[0:3])  # ['Radek', 'Maciek', 'MArek'] 0,1,2
print(lista[2:])  # ['MArek', 'Marta', 'Zenek', 'Jaśko', 'Radek', 'Adam']
print(lista[:3])  # ['Radek', 'Maciek', 'MArek']

print(lista[1:3])  # ['Maciek', 'MArek']
print(lista[8:10])  # []
print(lista[7:10])  # ['Adam']

# zamiana Zenek na mikołaja, indeks numer 2
lista[2] = "Mikołaj"

print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Marta', 'Zenek', 'Jaśko', 'Radek', 'Adam']

# wstawic elemnt pomiedzy inne
lista.insert(1, "Marcin")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Marta', 'Zenek', 'Jaśko', 'Radek', 'Adam']

# indeks danego elemntu
ind = lista.index("Zenek")
# usunięcie po indeksie
print(lista.pop(ind))  # Zenek - pop zwraca usunięty elemnt

# usuniecie po elemencie
lista.remove("Marta")
print(lista.remove("Adam"))  # None, remove zwraca None - nie ma potrzeby wypisywania co usunęliśmy

print(lista)

print(lista.index("Radek"))  # 0 pierwszy z brzegu
lista.remove("Radek")  # usunęło pierwszego od lewej
print(lista)  # ['Marcin', 'Maciek', 'Mikołaj', 'Jaśko', 'Radek']

print("Radek" in lista)  # True
# lista.remove("Adam")  # ValueError: list.remove(x): x not in list
print(lista.count("Radek"))  # 1

a = 1
b = 3
a = b  # nadpisane a
print(a)  # 3
a = 7
print(b)  # 3

lista2 = lista  # kopia referencji (kopia adresu pamięci)
print(lista2)
print(lista)
lista3 = lista.copy()  # kopia elemntów listy do nowej listy
lista2.clear()  # usuniecie elemntów z listy
print(lista2)  # []
print(lista)  # []
print(lista3)  # ['Marcin', 'Maciek', 'Mikołaj', 'Jaśko', 'Radek']
# id() - adres pamieci dla listy
print(id(lista))  # 2284422746496
print(id(lista2))  # 2284422746496
print(id(lista3))  # 2896029266432
# 15:00

liczby = [54, 999, 34, 22, 13.34, 687]
# liczby = [54, 999, 34, 22, 13.34, 687, "A"]  # TypeError: '<' not supported between instances of 'str' and 'int'
print(type(liczby))  # <class 'list'>
liczby.sort()  # sortowanie listy
print(liczby)  # [13.34, 22, 34, 54, 687, 999]

lista_osoby = ['radek', 'ola']
lista_osoby.sort()
print(lista_osoby)  # ['ola', 'radek']

liczby[3] = 6666
# wypisac elemnty tel listy liczby po ujemnych indeksach
# sprawdzic długośc listy
print(liczby)  # [13.34, 22, 34, 6666, 687, 999]
print(len(liczby))  # 6
print(liczby[-1])  # 999
print(liczby[-6])  # 13.34

print(liczby[0:3])  # [6666, 687, 999]

print(liczby[-3:])  # [6666, 687, 999]

liczby.remove(34)
print(liczby)  # [13.34, 22, 6666, 687, 999]

print(liczby.pop(2))  # usunęliśmy 6666

tekst = "Python"
lista1 = list(tekst)  # rozpakowanie sekwencji, odpowiednik extends()
print(lista1)  # ['P', 'y', 't', 'h', 'o', 'n']

# lista2 = []
# lista2.append(tekst)
lista2 = [tekst]  # odpowiednik append
print(lista2)  # ['Python']

print(lista1 + lista2)  # ['P', 'y', 't', 'h', 'o', 'n', 'Python']

# krotka - tupla
krotka = tuple(lista1)
print(krotka)  # ('P', 'y', 't', 'h', 'o', 'n')
