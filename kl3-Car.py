class Car:
    """klasa opisująca samochód w Pythonie"""

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0  # pole prywatne - hermetyzacja

    def gaz(self):  # setter
        self.__predkosc += 10
        self.__zmien_bieg()

    def licznik(self):  # getter, enkapsulacja - wystawianie w sposob kontrolowany pól, tylko tych koniecznych
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10

    def __zmien_bieg(self):
        print("Zmiana biegu")


car1 = Car("Opel", 2023)
print(car1.__doc__)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# po oznaczeniu pola jako prywatne, nie mozna odczytac predkosc
# print(car1.__predkosc)  # 50 AttributeError: 'Car' object has no attribute '__predkosc'.
# Did you mean: '_Car__predkosc'?
car1.licznik()  # Prędkość wynosi 50 km/h
car1.__predkosc = 0  # pole globalne
car1.licznik()  # Prędkość wynosi 50 km/h
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  # Prędkość wynosi 0 km/h
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Prędkość wynosi 50 km/h
# Prędkość wynosi 50 km/h
# Prędkość wynosi 0 km/h
