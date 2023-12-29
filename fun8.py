def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("kwargs", kwargs)
    print("args", args)


allparams(1, 2)  # a, b 1 2
allparams(1, 2, 6)  # c, d 6 256
allparams(1, 2, c=6)  # c, d 6 256
# allparams(a=1, b=2, c=6)  # TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
# / - oddziela argumenty mozliwe do przekazania po nazwie od tych co moga byc tylko pozycyjnie
# pozycyjne / pozycyjne lub po nazwie
allparams(1, 2, a=8)  # kwargs {'a': 8}
# allparams(1, 2, c=4, 5, 6, 7, 8, 9, 0, 0)  # SyntaxError: positional argument follows keyword argument
allparams(1, 2, 4, 5, 6, 7, 8, 9, 0, 0)  # c, d 4 256, args (5, 6, 7, 8, 9, 0, 0)
allparams(1, 2, 4, 5, 6, 7, 8, 9, 0, 0)  # c, d 4 256, args (5, 6, 7, 8, 9, 0, 0)
# d musi byc przekazane po nazwie, trafi do parametru d a nie do **kwargs
allparams(1, 2, 4, 5, 6, 7, 8, 9, 0, 0, d=78)  # c, d 4 78
allparams(1, 2, 4, 5, 6, 7, 8, 9, 0, 0, d=78, e=89, name="Radek", a=9)
# kwargs {'e': 89, 'name': 'Radek', 'a': 9}
