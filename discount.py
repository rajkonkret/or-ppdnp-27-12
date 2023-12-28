from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-12-28

time = datetime.now()
print(time)  # 2023-12-28 15:03:37.583314

print(time.hour)
print(today.day)

formatted_date = datetime.now().strftime("%d/%m/%Y")
print(formatted_date)  # 28/12/2023

formatted_time = datetime.now().strftime("%H:%M")
print(formatted_time)  # 15:05

formated_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(formated_datetime)  # 2023-12-28 15:06:48

# days = 0, seconds = 0, microseconds = 0,
# milliseconds = 0, minutes = 0, hours = 0, weeks = 0
tommorow = today + timedelta(days=1)
print(tommorow)  # 2023-12-29

# dla produktow z data waznosci today obnizymy cene o 20%

products = [
    {'sku': 1, 'exp_date': today, "price": 200},
    {'sku': 2, 'exp_date': today, "price": 100.0},
    {'sku': 3, 'exp_date': tommorow, "price": 55.50},
    {'sku': 4, 'exp_date': today, "price": 17},
]

for product in products:
    # print(product['price'])  # {'sku': 1, 'exp_date': datetime.date(2023, 12, 28), 'price': 200}
    if product['exp_date'] != today:
        continue  # wraca na poczatek petli, bierze kolejny element
    product['price'] *= 0.8
    print(f"""
Price for sku {product['sku']}
is now {product['price']}""")

# Price for sku 1
# is now 160.0
#
# Price for sku 2
# is now 80.0
#
# Price for sku 4
# is now 13.600000000000001
