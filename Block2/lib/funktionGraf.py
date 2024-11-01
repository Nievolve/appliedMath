import numpy as np
import matplotlib.pyplot as plt

# Funktionsregel
def f(x):
    return x + 2

# Skapa x-värden
h = 3
w = h*2-0
x = np.linspace(-3, 3, 100)
y = f(x)

# Skapa figur och axlar
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(x, y, color="red", linewidth=2, label="f(x) = x + 2")

# Anpassa axlarna och koordinatssystemet
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axhline(0, color="black", linewidth=0.5)  # x-axeln
ax.axvline(0, color="black", linewidth=0.5)  # y-axeln

# Lägg till rutnät
ax.grid(True, which='both', color=(0.776, 0.776, 0), linestyle='-', linewidth=0.5)
ax.set_aspect('equal', 'box')

# Visa etiketter på axlar
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

# Visa plott
plt.legend()
plt.show()
