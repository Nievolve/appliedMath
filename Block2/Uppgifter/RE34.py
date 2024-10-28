import numpy as np
import matplotlib.pyplot as plt
from lib import xyPlot as xy

# Funktion för att beräkna toppspänningen
def Ctopp(t):
    Ut = 325  # V
    w = 100 * np.pi  # Angular frequency
    top = Ut * np.sin(w * t)  # Sinusvåg, t i millisekunder
    return top

# Skapar listor för tid och spänning
interval = np.arange(-0.02, 0.021, 0.001)

resultat = [Ctopp(t) for t in interval]

for k in resultat:
    print(k)
yLabel= "Spänning"
xy.xyplot(resultat, len(resultat)+1, yLabel)