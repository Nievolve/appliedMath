import numpy as np
import matplotlib.pyplot as plt

# Konstanter
utopp = 325
w = 100 * np.pi
R = 2

# Definiera funktionerna u(t) och i(t)
def u(t):
    return utopp * np.sin(w * t * 10**-3)

def i(t):
    return u(t) / R

# Beräkna perioden
T = 2 * np.pi * 10**3 / w

# Skapa tidsvektor för plottning (0 till 2T)
t = np.linspace(0, 2 * T, 1000)

# Beräkna värden för u(t) och i(t)
u_values = u(t)
i_values = i(t)

# Skapa figur och axlar
fig, ax = plt.subplots(figsize=(10, 6))

# Plotta u(t) och i(t)
ax.plot(t, u_values, color="red", linewidth=2, label="u(t) [V]")
ax.plot(t, i_values, color="blue", linewidth=2, label="i(t) [A]")

# Anpassa axlarna och koordinatsystemet
ax.set_xlim(0, 2 * T)
ax.set_ylim(-400, 400)
ax.axhline(0, color="black", linewidth=0.5)  # x-axeln
ax.axvline(0, color="black", linewidth=0.5)  # y-axeln

# Lägg till rutnät
ax.grid(True, which='both', color=(0.776, 0.776, 0), linestyle='-', linewidth=0.5)
ax.set_aspect('auto')

# Visa etiketter på axlar
ax.set_xlabel("t [ms]")
ax.set_ylabel("u(t) [V]; i(t) [A]")

# Visa legend
plt.legend()

# Visa plott
plt.show()
