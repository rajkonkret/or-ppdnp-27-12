wiek = 47
rok = 2023
temp = 36.6

print(type(wiek))  # <class 'int'>
print(5 * wiek)  # 235
print(5 * "wiek")  # wiekwiekwiekwiekwiek

print(wiek * rok)
print(wiek + rok)
print(wiek - rok)
print(wiek / rok)  # dzielenie zwraca float -> 0.023232822540781017
print(wiek // rok)  # 0 - częśc całkowita z dzielenia
print(wiek % rok)  # modulo, reszta z dzielenia  47
print(5 // 2)  # 2 całkowite
print(5 - (5 // 2) * 2)  # reszta 1
# bo 2 * 2 =4, 5 - 4 = 1 reszta 1
# 5 % 2 = reszta 1 to liczba nieparzysta
# gdy 4 % 2 = reszta 0 to liczba parzysta
print(wiek ** rok)  # potegowanie
print(len(str(wiek ** rok)))  # 3383 - długosc wyniku tego potęgowania

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - (5 * 43) + (4 / 2 + 4) / 2)  # -158.0

print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# 1.02343247238 x 2 ** 22323
# liczby float wprowadzaja błąd zaokrąglenie

# typ logiczny
# prawda, fałsz
# True, False
czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
czy_znasz_pythona = False
print(czy_znasz_pythona)  # False
print(type(czy_znasz_pythona))  # <class 'bool'>
print(int(czy_znasz_pythona))  # 0 - False
print(int(True))  # 1

print(bool(1))  # True
print(bool(100))  # True
print(bool(-5))  # True
print(bool("radek"))  # True

print(bool(0))  # False
print(bool(''))  # False
print(bool(None))  # False , None - nic

print(bool(3.0 / 3))  # True
print(0 / 3)
print(bool(0 / 3))  # False

#
