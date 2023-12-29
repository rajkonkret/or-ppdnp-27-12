# funkcja zagnieżdzona, funkcja wewnętrzna
# dekorator wykorzystuje mechanizm funkcji wewnętrznej
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwracamy adres fun2 (referencje)


# nazwa funkcji i nawiasy ()
print(fun1())  # <function fun1.<locals>.fun2 at 0x000001805E5E8CC0>
xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x0000019532808CC0>
print(type(xFun))  # <class 'function'>
xFun()  # uruchomienie funkcji xFun czyli de facto fun2 bo to sie tam znajduje
# To jest fun2
# 11:25
