def connect(**opcje):  # argumenty słownikowe - tu trafiają argumenty przekazane po nazwie
    print(opcje)
    connect_param = {
        'host': '127.0.0.1'
    }
    connect_param['pwd'] = opcje
    print(connect_param)  # {'host': '127.0.0.1', 'pwd': {'a': 8}}


def all_p(*args, **kwargs):  # przyjmie argumenty pozycyjne i nazwane
    print(args, kwargs)


connect()  # {} - pusty słownik
connect(a=8)  # {'a': 8}
all_p(1, 2, 3, 4, 5, 6, a=7, i=0, cena=1000)
# (1, 2, 3, 4, 5, 6) {'a': 7, 'i': 0, 'cena': 1000}
print(1, 2, 3, 4, 5, "A")  # 1 2 3 4 5 A
print(1, 2, 3, 4, 5, "A", sep=";")  # 1;2;3;4;5;A
