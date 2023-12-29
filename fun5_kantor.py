# funkcje kantor
# usd, eur

def kantor(waluta):
    """
    Funkcja zwraca kantor przeliczający daną walutę
    :param waluta: kod waluty
    :return: funkcje przeliczajaca wskazana walute
    """
    print("Uruchomienie kantora")

    def eur(kwota=0):
        print(f"Wymieniam  {kwota} euro na {kwota * 4.35}")

    def usd(kwota=0):
        print(f"Wymieniam  {kwota} usd na {kwota * 3.93}")

    if waluta == 'eur':
        return eur
    else:
        return usd


kantor_usd = kantor('usd')
print(kantor_usd)
print(type(kantor_usd))
kantor_usd()
# print(kantor.__doc__)  Dokumentacja naszej funkcji
# print(print.__doc__)
# przerobic tak by funkcje usd,eur otrzymywały kwote
# wypisac przeliczona kwote
kantor_usd(1000)
# Wymieniam  1000 usd na 3930.0

kantor_eur = kantor('eur')
kantor_eur(250)
# Wymieniam  250 euro na 1087.5
