# wyjatki - błedy działania programu
# przechwytujemy wyjatek po to by program nie zakończył nieoczkiwanie działąnia
# obsługujemy wyjątek w sposób dla nas właściwy

try:
    # print(2 / 0)  # ZeroDivisionError: division by zero
    # print("a" + 0)  # Błąd typu
    # print(int("a") + 0)  # Bląd wartosci
    print(0)  #
except ZeroDivisionError:
    print("Nie dziel przez zero")
except ValueError:
    print("Bląd wartosci")
except TypeError:
    print("Błąd typu")
except Exception as e:
    print("Bład", e)
else:
    print("Gdy bład nie wystapił")
finally:
    print('Wykona się zawsze')

print("Program działa nadal")
# Bład division by zero
# Program działa nadal
# Nie dziel przez zero
# Program działa nadal
# try - except - [else - finally]
