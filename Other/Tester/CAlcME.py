import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, sin, cos, pi, deg

# Precision
np.set_printoptions(precision=2)

# Definiera parametrar
w = 100 * np.pi

# Definiera funktionerna för ström
def i1(t):
    return 2 * np.sin(w * t)

def i2(t):
    return 1.5 * np.sin(w * t - 3 * np.pi / 4)

# Tidsrepresentation
interval = np.linspace(0, 10 / 3, 100)
i1_vals = [i1(t_val) for t_val in interval]
i2_vals = [i2(t_val) for t_val in interval]

# Plottning av i1 och i2
plt.plot(interval, i1_vals, label='i1(t)', color='red', linewidth=2)
plt.plot(interval, i2_vals, label='i2(t)', color='blue', linewidth=2)
plt.xlabel("Tid [s]")
plt.ylabel("Ström [A]")
plt.legend()
plt.grid(True)
plt.show()

# Addition av strömmarna
def i3(t):
    return i1(t) + i2(t)

i3_vals = [i3(t_val) for t_val in interval]

# Plottning av i3
plt.plot(interval, i3_vals, label='i3(t)', color='green', linewidth=2)
plt.xlabel("Tid [s]")
plt.ylabel("Ström [A]")
plt.legend()
plt.grid(True)
plt.show()

# Fasvinkelberäkning
i3_topp = 3.2
beta3 = symbols('beta3')
eq_beta3 = Eq(3.2 * sin(beta3), 1.1)
beta3_sol = solve(eq_beta3, beta3)
beta3_deg = [float(deg(sol)) for sol in beta3_sol]  # Omvandla radianer till grader

print(f"i3 topp = {i3_topp}")
print(f"beta3 ≈ {beta3_deg[0]:.1f}°")  # Välj en lösning för att visa

# Polar representation
I1_polar = complex(2 * np.cos(0), 2 * np.sin(0))
I2_polar = complex(1.5 * np.cos(-3 * np.pi / 4), 1.5 * np.sin(-3 * np.pi / 4))
I3_polar = I1_polar + I2_polar

# Argument (fasvinkel) och magnitud för i3 i grader
I3_magnitude = abs(I3_polar)
I3_angle_deg = np.degrees(np.angle(I3_polar))

print(f"I3 toppvärde: {I3_magnitude:.2f} A")
print(f"I3 fasvinkel: {I3_angle_deg:.1f}°")

# Plottning av polar form
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot([0, 0], [0, I3_magnitude], label='I3', color='black', linewidth=3)
ax.plot([0, np.radians(beta3_deg[0])], [0, I3_magnitude], label='I3 Approx', color='blue', linewidth=3)
ax.set_title("Fasor i Polar Representation")
ax.legend()
plt.show()