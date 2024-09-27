import numpy as np
import matplotlib.pyplot as plt

# Definiera funktionerna
def avståndSecond(d):
    eta2 = 2.1 * eta0/1000
    A = 0.5/100  # Meter**2
    C2 = eta2 * A / d
    return C2

def avståndFirst(d):
    eta1 = 2.9 * eta0/1000
    A = 0.5/100  # Meter**2
    C1 = eta1 * A / d
    return C1

# Konstanter
eta0 = 8.85 * 10**-12  # Farad/Meter

# Skapa listan dlist
dlist = np.arange(0.5, 5.5 + 0.1, 0.1)

# Beräkna kapacitansvärden för varje d
C1_values = [avståndFirst(d) for d in dlist]
C2_values = [avståndSecond(d) for d in dlist]

# Plotting
plt.plot(dlist, C1_values, label="avståndFirst", color='b')
plt.plot(dlist, C2_values, label="avståndSecond", color='r')

# Anpassa grafen
plt.xlabel("Avstånd (mm)")
plt.ylabel("Kapacitans (mF)")
plt.title("Kapacitansutveckling för avståndFirst och avståndSecond")
plt.legend()
plt.grid(True)

# Visa grafen
plt.show()












