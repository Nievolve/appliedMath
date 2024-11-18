import matplotlib.pyplot as plt
import numpy as np

# Genererar en plotter utifrån en lista

def listPlotter(listToDisplay):
    x = np.linspace(0, round(len(listToDisplay)), len(listToDisplay))

    # Skapa plotten
    plt.figure()

    # Rita kurvan
    plt.plot(x, listToDisplay, label="Imported")

    # Lägg till etiketter och titel
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Graf")
    plt.legend()

    # Visa grafen
    plt.grid(True)
    plt.show()

def visarPlotter():
    pass

if __name__ == "__main__":
    visarPlotter()