from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkoscia", self.szybkosc)

    @abstractmethod  # dekorator metody abstrakcyjnej
    def wydaj_odglos(self):
        pass


class Kura(Ptak):  # dziedziczymy po klasie Ptak
    """
    Klasa kura
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    # Poniewaz metoda wydaj_odglos jest abstrakcyjna musimy w klasach dziedziczących
    # ją nadpisać
    def wydaj_odglos(self):
        print("ko ko ko ko kok ko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


class Orzel(Ptak):

    def wydaj_odglos(self):
        print("kier kir kier")

    def polowanie(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")


# po dodaniu @abstractmethod klasa stała się abstrakcyjna
# dosatjemy błąd
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# nie można utworzyc obiektów tej klasy
# or1 = Ptak("Orzel", 30)
# or1.latam()
# or1.wydaj_odglos()
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkoscia 0
# kur1.wydaj_odglos()

kur2 = Kura("Kura")  # def __init__(self, gatunek):
kur2.latam()  # Tu Kura Ja nie latam
kur2.wydaj_odglos()
kur2.dziobanie()

or2 = Orzel("Orzel Bielik", 45)
or2.latam()
or2.wydaj_odglos()
or2.polowanie()

# # polimorfizm
# lista_ptakow = [or1, kur1, kur2]
# for p in lista_ptakow:
#     p.latam()

# Tu Kura Ja nie latam
# ko ko ko ko kok ko
# Tu Kura Idę sobie podziobać
# Tu Orzel Bielik Lecę z szybkoscia 45
# kier kir kier
# Tu Orzel Bielik Rozpoczynam polowanie
