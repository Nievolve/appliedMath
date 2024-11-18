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



def plotLines(xLength, yLength):
    # Skapa linjen längs x-axeln
    x1 = [0, xLength]  # Från 0 till xLength
    y1 = [0, 0]        # Y är konstant 0

    # Skapa linjen längs y-axeln
    x2 = [xLength, xLength]  # X är konstant vid xLength
    y2 = [0, yLength]        # Från 0 till yLength

    # Plotta båda linjerna
    plt.figure()
    plt.plot(x1, y1, label="Linje utmed x-axeln", color="blue")
    plt.plot(x2, y2, label="Linje utmed y-axeln", color="red")

    # Lägg till etiketter och titel
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Linjer utmed x- och y-axeln")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Markera x-axeln
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Markera y-axeln
    plt.legend()
    plt.grid(True)

    # Visa grafen
    plt.show()




if __name__ == "__main__":
    plotLines(xLength=5, yLength=-2)