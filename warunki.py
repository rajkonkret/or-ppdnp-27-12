# instrukcje warunkowe - instrukcje sterowania przepływem programu
# if

# odp = True
# # if działa tak, ze sprawdza warunek
# # jesli warunek jest prawdziwy wykonuje instrukcje po :
# # odp = False  # pułapka
# if odp:  # jesli warunek spełniony
#     print("Brawo")  # po : obowiązkowe wciecie (4 spacje) i minimum jedna instrukcja
# else:  # w przeciwnym przypadku
#     print("Musisz uczyć sie dalej")
#
# print("Dalsza częśc programu")

# podatek = 0.0
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.7
#
# # kolejność warunków ma znaczenie
# print(f"Zapłacisz {zarobki * podatek} zł.")
# # dodac podatek 0.2 dla dochodow od 10000 do 29999

suma_zam = 250
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0

rabat = 25 if suma_zam > 150 else 0

print(f"Rabat wynosi {rabacik}")
print(f"Rabat wynosi {rabat}")
# 11:30

lista_bledow = []
alert_system = 'email'
error = 'jakis inny'

error_message = "Stało się coś strasznego"

if alert_system == 'console':  # porównanie
    print(error_message)
elif alert_system == 'email':
    lista_bledow.append('email')
    if error == 'medium':
        lista_bledow.append('medium')
    elif error == 'critical':
        lista_bledow.append('krytyczny')
    else:
        lista_bledow.append('inny')

else:
    print("System nieznany")

print(lista_bledow)

a = 14
b = 3
print(f"")