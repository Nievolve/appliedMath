import numpy as np
import matplotlib.pyplot as plt

# Funktion för att beräkna toppspänningen
def Ctopp(t):
    Ut = 325  # V
    w = 100 * np.pi  # Angular frequency
    top = Ut * np.sin(w * t * 10**-3)  # Sinusvåg, t i millisekunder
    return top

# Skapar listor för tid och spänning
time_list = []
voltage_list = []

# Fyller listorna med värden
for k in range(1, 200):  # Kanske vill du använda fler punkter för en mer jämn kurva
    voltage = Ctopp(t=k)
    time_list.append(k)
    voltage_list.append(voltage)

# Plotter
plt.plot(time_list, voltage_list, label="Spänning över tid")

# Lägg till rubriker och etiketter
plt.title('Toppvärde av spänning över tid')
plt.xlabel('Tid (ms)')
plt.ylabel('Spänning (V)')

# Visa en legend
plt.legend()

# Visa grafen
plt.show()
