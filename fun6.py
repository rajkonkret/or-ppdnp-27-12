# funkcje obliczającą średnia np.: ocen
# ile argumentów powinna przyjąć funkcja?
# nieskonczona liczba argumentów
def liczby(*cyfry):  # * - moze przyjąć dowolną ilość argumentów pozycyjnych
    print(cyfry)
    print(type(cyfry))  # <class 'tuple'>
    suma = 0
    print(sum(cyfry))  # sum() - suma z elementów kolekcji
    try:
        for c in cyfry:
            suma += c
        count = len(cyfry)
        # print(f"Średnia wynosi {suma / count}")
        avg = suma / count
    except Exception as e:
        print("bład", e)
    else:
        print(f"Średnia wynosi {avg}")
    finally:
        print("Zakończyłem obliczenia")


liczby()  # ()
liczby(1)
liczby(1, 2, 3)
liczby(1, 2, 3, 4, 5, 6)
# ()
# (1,)
# (1, 2, 3)
# (1, 2, 3, 4, 5, 6)
