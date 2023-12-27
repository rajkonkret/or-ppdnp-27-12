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
print(int(14) + int(34))  # 48
# str() - zamiana na string
print(str(14) + "34")  # 1434