# krotka (tupla)  - kolekcja niemutowalna
# nie można zmienić elementów tej kolekcji
# krotka jednoelementowa to odpowiednik zmiennej niezmiennej czyli stałej...

tupla = "Radek"
print(type(tupla))  # <class 'str'>
tupla1 = ("Radek",)  # nawiasy opcjonalne, przecinek po pierwszym elemencie obowiązkowy
print(type(tupla1))  # <class 'tuple'>
tupla2 = "Tomek", "Radek", "Zenek", "Marek", "Marta"
print(type(tupla2))  # <class 'tuple'>

tupla3 = 43, 55, 22.34, 11, 200
print(tupla3)  # (43, 55, 22.34, 11, 200)
print(type(tupla3))  # <class 'tuple'>

temp = 36, 6
print(type(temp))  # <class 'tuple'>
print(temp)  # (36, 6)

print(tupla2.count("Tomek"))  # 1
print(tupla2.index("Tomek"))  # 0

# rozpakowanie krotki
a, b = 1, 2
# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)

a, *b = 1, 2, 3  # * - worek na pozostałe dane
print(a, b)  # 1 [2, 3]

imie1, *imie2, imie3 = tupla2
print(imie1, imie2, imie3)  # Tomek ['Radek', 'Zenek', 'Marek'] Marta

*imie1, imie2, imie3 = tupla2
print(imie1, imie2, imie3)  # ['Tomek', 'Radek', 'Zenek'] Marek Marta

imie1, imie2, *imie3 = tupla2
print(imie1, imie2, imie3)  # Tomek Radek ['Zenek', 'Marek', 'Marta']

lista = list(tupla3)
print(lista)  # [43, 55, 22.34, 11, 200]
print(type(lista))  # <class 'list'>
