import random

# random - słuzy do dziłań z liczbami pseudolosowymi

print(random.randint(1, 6))  # int 1..6
print(random.random())  # 0.9994698872825422 float 0..0,999999
print(random.random() * 6)  # 3.3949735388687223 float 0..5,999
print(random.randrange(6))  # int 0..5
print(random.randrange(1, 6))  # int 1..5

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))  # 34

lista_lotto = list(range(1, 50))  # 1..49
print(lista_lotto)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)
wyn = random.choice(lista_lotto)
lista_lotto.remove(wyn)
print(wyn)

print(random.choices(lista_lotto, k=6))  # losuje 6 liczb ale z powtórzeniami [31, 30, 28, 27, 31, 8]
print(random.sample(lista_lotto, 6))  # [16, 37, 15, 46, 47, 27] losuje bez powtórzeń
print(random.sample(lista_lotto, k=6))  # [10, 42, 8, 41, 24, 13] losuje bez powtórzeń
k = 3
print(random.sample(lista_lotto, k=k))  # [8, 49, 21]
