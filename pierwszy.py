print()  # wypisz/wydrukuj
print()  # tab
# ctrl alt l - układa kod wg zasad pep8 - formatuje do ładnej postaci
# 11:30
print("Nazywam się Radek")  # Nazywam się Radek
print('Nazywam się Radek')  # Nazywam się Radek
# - znaczek komentarza #

# type() - sprawdzanie typu
print(type("Radek"))  # <class 'str'> - tekst

print(39)
print(type(39))  # <class 'int'> - liczby całkowite

print(type('39'))  # <class 'str'>
# konkatenacja stringów - łączenie tekstów
print(5 * "14")  # 1414141414
print("14" + "34")  # 1434
# print(14 + "34")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# silne typowanie, sam nie zamienia typów
# int() - rzutowanie na liczby
print(int("14") + int("34"))  # 48
# str() - zamiana na string
print(str(14) + "34")  # 1434

# zmienna - pudełko na dane
imie = "Radek"
# wypisanie zawartość zmiennej
print(imie)  # Radek
print(type(imie))  # <class 'str'>
imie = 39
print(imie)
print(type(imie))  # <class 'int'>
imie = "Tomek"
print(type(imie))  # <class 'str'>
# print(imie + 12)  # TypeError: can only concatenate str (not "int") to str
# print(int(imie) + 12)  # ValueError: invalid literal for int() with base 10: 'Tomek'
print(imie * 12)  # TomekTomekTomekTomekTomekTomekTomekTomekTomekTomekTomekTomek
# ctrl / - komentarz w linii w której znajduje się kursor

wiek = 48  # int
print(wiek + 12)  # 60
