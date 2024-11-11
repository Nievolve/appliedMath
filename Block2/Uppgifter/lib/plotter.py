import matplotlib.pyplot as plt
import numpy as np

# Genererar en plotter utifrån en lista

def listPlotter(listToDisplay):
    x = np.linspace(0, len(listToDisplay), len(listToDisplay))

    # Skapa plotten
    plt.figure()

    # Rita kurvan
    plt.plot(x, listToDisplay, label="")

    # Lägg till etiketter och titel
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Graf")
    plt.legend()

    # Visa grafen
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    pass