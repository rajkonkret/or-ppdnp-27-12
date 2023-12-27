import sys

user = "Tomek"  # str
wiek = 39  # int
wersja = 3.1100001  # float - liczby zmiennoprzecinkowe
liczba = 134567890123  # int

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
print(
    sys.int_info)  # sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300, str_digits_check_threshold=640)

print("Witaj %s, masz teraz %d lat" % (user, wiek))  # Witaj Tomek, masz teraz 39 lat
# %s - string
# %d - digit
# Przy wypisywaniu z % sprawdza typ !!!
# print("Witaj %d, masz teraz %s lat" % (user, wiek))  # TypeError: %d format: a real number is required, not str
# Witaj Tomek, masz teraz 39 lat
print("Witaj %(user)s, masz teraz %(age)d lat" % {'user': user, 'age': wiek})

print("Witaj {}, masz teraz {} lat".format(user, wiek))  # Witaj Tomek, masz teraz 39 lat

print(f"Witaj {user}, masz teraz {wiek} lat.")
# f - fstring - tekst sformatowany
