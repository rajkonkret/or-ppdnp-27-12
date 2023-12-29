# klasy - szablon, wzór określający cechy i funkcjonalności jakie bedzie posiadał obiekt
# obiekt - instancja klasy - element zbudowany wg schematu jaki ma klasa

# definicja klasy
class Human:
    """
    Klasa opsiująca człowieka w Pythonie
    """
    imie = ""
    plec = "k"
    wiek = 29


# tworzymy obiekt klasy
cz1 = Human()
print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)
cz1.imie = "Magda"
print(cz1.imie)

cz2 = Human()
cz2.imie = 'Radek'
cz2.wiek = 78
cz2.plec = "m"

print(cz2.imie)  # " Radek"
