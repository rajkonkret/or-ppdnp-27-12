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
    5. Koniec
    """)
    odp = input("Podaj operację do wykonania")

    if odp == "5":
        break
