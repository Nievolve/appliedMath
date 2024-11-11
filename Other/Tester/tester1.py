import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def iCalc1(w, t):
    i1 = 2 * np.sin(w * t + (np.pi / 6))
    return i1

def iCalc2(w, t):
    i2 = 4 * np.sin(w * t + (4 * np.pi / 9))
    return i2
def xyplot(y, L, yLabel):


    # X Axel
    x = list(range(1, L))  # X axelns längd


    #Läser in en range 
    plt.plot(x, y, label=yLabel)

    # Sätt etiketter för axlarna
    plt.xlabel(" ")
    plt.ylabel(yLabel)

    # Sätt en titel
    plt.title(yLabel)

    # Ange att varje nivå ska ha en tick
    plt.xticks()  # Detta kommer att visa varje nivå

    # Aktivera rutnät
    plt.grid(True)

    # Visa en legend
    plt.legend()

    # Visa grafen
    plt.show()
i3 = np.sqrt(2**2 + 4**2 - 2 * 2 * 4 * np.cos(np.deg2rad(130)))
print(f"{i3:.3g}")

w = 100 * np.pi
range = np.arange(-0.020, 0.041, 0.001)  # Ändrat stoppvärde

i3List = [iCalc1(w, k) + iCalc2(w, k) for k in range]

for k in i3List:
    print(k)

titel = "Titel"


