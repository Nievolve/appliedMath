# Detta program beräknar och plottar sinusformade strömmar över tid, givet olika initialparametrar.
# Det definierar tre olika sinusformade strömvågor (I1, I2 och I3) och beräknar sedan
# den resulterande vågformen av I3 som är en kombination av I1 och I2(Kirchoffslag). Maximalvärdet för I3-vågformen
# beräknas också.

import numpy as np
import matplotlib.pyplot as plt

# Funktion för att beräkna sinusformad ström
def Icalc(itopp, t, w, V):
    return itopp * np.sin(w * t + V)

# Funktion för att hitta toppvärdet i en given array
def top(x):
    y = max(x)
    return y

# Givna värden
w = 100 * np.pi  # Vinkelhastighet (rad/s)
interval = np.arange(0, 0.1, 0.001)  # Tidsintervall från 0 till 0,1 sekunder, med steg om 0,001 sekunder

# Beräkna strömvärden för varje vågform
I1Graf = [Icalc(itopp=2, t=k, w=w, V=0) for k in interval]  # Ström I1 med toppvärde 2A, ingen fasförskjutning
I2Graf = [Icalc(itopp=1.5, t=k, w=w, V=np.sqrt(2)/2) for k in interval]  # Ström I2 med toppvärde 1,5A, fasförskjutning av sqrt(2)/2
I3Graf = [Icalc(itopp=1.5, t=k, w=w, V=np.sqrt(2)/2) + Icalc(itopp=2, t=k, w=w, V=0) for k in interval]  # Summan av I1 och I2

# Skriv ut maximalvärdet för den kombinerade vågformen I3
print(f"Max är: {top(I3Graf):.3g} A")


# Plotta resultaten
plt.plot(interval, I1Graf, label="I1")  # Plotta I1
plt.plot(interval, I2Graf, label="I2")  # Plotta I2
plt.plot(interval, I3Graf, label="I3")  # Plotta I3 (resulterande vågform)

# Märk axlarna
plt.xlabel("Tid (sekunder)")  # Tid i sekunder
plt.ylabel("Ström (A)")  # Ström i ampere

# Lägg till en titel till grafen
plt.title("Sinusformad Ström över Tid")  # Sinusformad ström över tid

# Aktivera rutnät och legend
plt.grid(True)
plt.legend()

# Visa grafen
plt.show()



