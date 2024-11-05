import numpy as np
import matplotlib.pyplot as plt  # Korrigerad import

# Definiera funktionen u(t)
def u(t):
    return 325 * np.sin(100 * np.pi * t + (np.pi / 4))

# Vinkelfrekvens
w = 100 * np.pi

# Intervall för tid
intervalT = np.arange(-0.02, 0.02, 0.001)

# Beräkna spänningen för varje tidpunkt i intervallet
ut = [u(k) for k in intervalT]

# Skapa en figur och axlar
fig, ax = plt.subplots()


ax.plot(intervalT, ut, label="u(t)")  # Använd intervalT som x-axel och ut som y-axel

ax.set_xlabel("tid [s]")
ax.set_ylabel("Spänning [V]")
ax.set_title("Graf av u(t)")
ax.legend()


plt.show()
