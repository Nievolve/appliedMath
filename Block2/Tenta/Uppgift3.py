import numpy as np
import matplotlib.pyplot as plt

# Funktion för spänning u(t)
def ut(utopp, f, alfa, t):
    return utopp * np.sin(f * t + alfa)

# u1 (parametrar)
u1Topp = 163
f1 = 70
alfa1 = 0  # Fasvinkel

# u2 (parametrar)
u2Topp = 228

f2 = 440
alfa2 = np.pi / 3  # Fasvinkel

# Tidsintervall
timeRange = np.arange(0, 0.03,0.001)  # Tid i sekunder

# Beräkna spänningar
u1List = ut(u1Topp, f1, alfa1, timeRange)
u2List = ut(u2Topp, f2, alfa2, timeRange)

# Skapa graf
plt.figure(figsize=(10, 6))
plt.plot(timeRange * 1000, u1List, label="U1(t) (163*sin(70πt))")
plt.plot(timeRange * 1000, u2List, label="U2(t) (228*sin(440t + π/3))", linestyle='--')

# Lägg till etiketter och titel
plt.xlabel("Tid (ms)")
plt.ylabel("Spänning (V)")
plt.title("Växelspänningar U1 och U2")
plt.legend()
plt.grid(True)

# Visa grafen
plt.show()
