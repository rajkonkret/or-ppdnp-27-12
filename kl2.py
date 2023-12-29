class Human:
    """
    Klasa opisujaca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, plec="k"):
        """
        Funkcja inicjalizujaca (konstruktor)
        :param imie:
        :param wiek:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat")


cz1 = Human('Anna', 34)
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)

cz1.powitanie()  # Nazywam się Anna
cz1.wypisz_wiek()  # Mam 34 lat

cz2 = Human("Radek", 34, "m")
cz2.powitanie()  # Nazywam się Radek

