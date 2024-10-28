import numpy as np

import matplotlib.pyplot as plt

exp = []
for k in range(1,100):
    #result = 0.25 * sum([ell + 300 * np.power(2, ell / 7) for ell in range(1, k)])
    result = 3+9*k*np.sqrt(k)
    exp.append(result)





# Exempeldata
levels = list(range(1, 100))  # Nivåer från 1 till 99


# Skapa en linjediagram
plt.plot(levels, exp, label="Samlad XP")

# Sätt etiketter för axlarna
plt.xlabel("Level")
plt.ylabel("Samlad XP")

# Sätt en titel
plt.title("Samlad XP för nivåer 1 till 99")

# Ange att varje nivå ska ha en tick
plt.xticks()  # Detta kommer att visa varje nivå

# Aktivera rutnät
plt.grid(True)

# Visa en legend
plt.legend()

# Visa grafen
plt.show()
