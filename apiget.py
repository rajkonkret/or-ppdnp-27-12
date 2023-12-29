# REST API
# HTTP GET,POST,PUT/PATCH,DELETE
# BAZA DANYCH - SELECT, INSERT, UPDATE, DELETE
# CRUD - CREATE, READ, UPDATE, DELETE
import requests as re

# pip install requests

url = "http://api.nbp.pl/api/exchangerates/rates/A/USD/"
response = re.get(url)
print(response)
# <Response [200]> ok
# 3xx - błedy przekierowania
# 4xx - 404 - brak zasobu, 400 Bad request
# 5xx 500 internal server Error
table = response.json()
print(table)
print(type(table))  # <class 'dict'>
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '251/A/NBP/2023', 'effectiveDate': '2023-12-29', 'mid': 3.935}]}
print(table.keys())  # dict_keys(['table', 'currency', 'code', 'rates'])
for k, v in table.items():
    print(k, "=>", v)
# table => A
# currency => dolar amerykański
# code => USD
# rates => [{'no': '251/A/NBP/2023', 'effectiveDate': '2023-12-29', 'mid': 3.935}]
print(table['code'])  # USD
print(table['rates'])  # [{'no': '251/A/NBP/2023', 'effectiveDate': '2023-12-29', 'mid': 3.935}]
print(table['rates'][0]['mid'])  # 3.935
