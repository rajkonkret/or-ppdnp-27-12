import matplotlib.pyplot as plt

# wykresy

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 9, 11]

plt.plot(x, y, color="red")
plt.title("Wykres liniowy")
plt.xlabel("Oś X")
plt.ylabel("OS Y")
plt.savefig("wykres.png")
plt.show()
