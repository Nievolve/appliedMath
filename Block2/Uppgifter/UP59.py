import numpy as np
import cmath as cm
import matplotlib.pyplot as plt
# Given information
R = 75.0  # Resistor i ohm (Ω)
L = 50.0e-3  # Induktans i henry (H)
C = 40.0e-6  # Kapacitans i farad (F)

# Frekvenslista
fList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
lenfList = len(fList)  # Längden
Zt = []
thetat = []
plotListA = []
plotListB = []


# Funktioner
def w(f):
    return 2 * np.pi * f

def Zl(f, L):
    # Impedansen för induktans(Complex)
    return 1j * w(f) * L

def Zc(f, C):
    # Impedansen för kapacitans(Complex)
    return 1 / (1j * w(f) * C)
def listPlotter(listToDisplay,scndList,thrList):
    x = np.linspace(0, round(len(listToDisplay)), len(listToDisplay))
    
    # Skapa plotten
    plt.figure()

    # Rita kurvan
    plt.plot(x, listToDisplay, label="Frekvens")
    plt.plot(x, scndList, label="Z_AB")
    plt.plot(x, thrList, label="Grader")
    # Lägg till etiketter och titel
    plt.xlabel('')
    plt.ylabel('Frekvens')
    plt.title("Graf")
    plt.legend()

    # Visa grafen
    plt.grid(True)
    plt.show()
# Beräkna för varje frekvens ur [fList]
for f in fList:
    Z_L = Zl(f, L)
    Z_C = Zc(f, C)
    Z_LC = Z_L + Z_C  # Seriekoppling av L och C
    Z_R = R
    Z_AB = (Z_R * Z_LC) / (Z_R + Z_LC)  # Parallellkoppling mellan R och LC

    Zt.append(abs(Z_AB))  # Magnituden av Z_AB
    thetat.append(np.angle(Z_AB, deg=True))  # Fasen av Z_AB i grader

    print(f"Frekvens: {f} Hz, |Z_AB|: {abs(Z_AB):.3g} Ω, Fasen: {np.angle(Z_AB, deg=True):.3g}°")

listPlotter(fList,Zt,thetat)
