# set, zbiór - przechowuje unikalne wartości
# tracimy kolejnośc przy dodawaniu elementów

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>
print(tuple(zbior))  # (33, 66, 777, 11, 44, 22, 55) - krotka

# do tworzenia pustego zbioru używamy słówka set()
zb2 = set()  # pusty zbiór
print(zb2)  # set() - pusty zbior

# dodawanie do zbioru
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(33)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

# usunięcie ze zbioru po elemencie
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22}

# usuniecie za pomoca pop() - usunie pierwszy element
print(zbior.pop())  # 33
print(zbior.pop())  # 66
print(zbior.pop())  # 777

print(zbior)  # {11, 44, 18, 22}

zbior2 = {66, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)  # {66, 18, 52, 999, 11, 44, 62}

# zbiory mozna porównywac
print(zbior | zbior2)  # lub, suma zbiorów {66, 999, 11, 44, 18, 52, 22, 62}
print(zbior & zbior2)  # i, częśc wspolna {18, 11, 44}
print(zbior)  # {11, 44, 18, 22}
print(zbior2)  # {66, 18, 52, 999, 11, 44, 62}

# różnica
print(zbior - zbior2)  # {22}
# {11, 44, 18, 22} - {66, 18, 52, 999, 11, 44, 62} = {22}
print(zbior.difference(zbior2))  # {22}
print(zbior2.difference(zbior))  # {66, 52, 62, 999}
print(len(zbior))
print(77 in zbior)  # False - sprawdzenie czy istnieje w zbiorze
