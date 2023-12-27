tekst = "Witaj świecie"
print(tekst)
print(type(tekst))  # <class 'str'>

tekst.upper()
""" Return a copy of the string converted to uppercase. """
print(tekst)  # Witaj świecie
tekst2 = tekst.upper()
print(tekst2)  # WITAJ ŚWIECIE
print(tekst)  # Witaj świecie
print(tekst.upper())  # WITAJ ŚWIECIE
# teksty w pythonie są niemutowalne
# lower()
print(tekst2.lower())  # zamian ana małe litery witaj świecie

print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst.removesuffix("świecie"))  # "Witaj "
tekst3 = "Witaj świecie świecie"
print(tekst3.removesuffix("świecie"))  # "Witaj świecie "# od 3 indeksu, indexy liczone od 0
print(tekst[3:])  # aj świecie

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
# b - postac bajtowa
# \x - kolejne znaki oznaczają wartośc bajtu w formie szesnastkowej
print(type(encoded_s))  # <class 'bytes'>
# odkodowanie do formatu naszego środowiska utf-8
print(encoded_s.decode('utf-8'))  # Witaj świecie

imie = "Radek"
print(imie.count("a"))
print(imie.count("a", 0, 3))  # 0,1,2 - te brane pod uwage
# 0 - R, 1 - a, 2 - d
print(imie.count("e", 0, 3))  # 0 bo literka e ma indeks 3, a zbiór z prawej otwarty,
# nie bierze pod uwagę indeksu 3
# długość tekstu len()
print(len(imie))  # 5

imie2 = "Żółw"
print(len(imie2))  # 4
# f-stringi - teksty sformatowae - f
tekst_format = f"Mam n a imię {imie} i lubię pythona."
print(tekst_format)  # Mam n a imię Radek i lubię pythona.
tekst_format2 = f"\tMam n a imię {imie}\n i lubię pythona.\b"
print(tekst_format2)
# "	Mam n a imię Radek
#  i lubię pythona"
# \t - tabulator
# \n - nowa linia
# \b - backspace
print("Radek \"tekst\"")  # Radek "tekst"
