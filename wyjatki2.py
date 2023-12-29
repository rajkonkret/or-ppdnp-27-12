# napisanie aplikacji kalkulator
# uzyc petli while jako głównej pętli programu
# ma miec opcje wyjscia z programu
# menu
# pobierac typ operacji
# ewentualnie pobrac liczby
# łądnie wypisać wynik

while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)
    odp = input("Podaj operację do wykonania")

    if odp == "5":
        break
    try:
        a = int(input("Podaj pierwszą liczbę"))
        b = int(input("Podaj drugą liczbę"))

        if odp == "1":
            print(f"Wynik dodawania {a} + {b} = {a + b}")
        elif odp == "2":
            print(f"Wynik odejmowania {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"Wynik mnożenia {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"Wynik dzielenia {a} / {b} = {a / b}")
        else:
            print("Nie znam takiego działania")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except ValueError:
        print("Bład wartości")
    except Exception as e:
        print("Bład", e)
    finally:  # wykonuje się zawsze
        print("Zakońćzone obliczenia")
# eval() eval()	Evaluates and executes an expression
print(eval("2 + 2"))
