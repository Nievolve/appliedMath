import numpy as np
import matplotlib.pyplot as plt

def f(x):
    #              Skriv in formel
    returnList = [3*k+(1/3) for k in x]
    listPlotter(returnList)
    return returnList
# InCode plotter funktion
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
# Sätt range av data 
x = np.arange(0.000,0.0020,0.001)
f(x)
