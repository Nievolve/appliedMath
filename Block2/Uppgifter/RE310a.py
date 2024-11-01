import numpy as np
import matplotlib.pyplot as plt

# Definiera funktionerna

def Ur(R, Itopp, w, t, V):
    return R * Itopp * np.sin(w * t + V)

def Uc(xc, Itopp, w, t, V, faskompensering):
    return xc * Itopp * np.sin(w * t - V + faskompensering)

def Xc(w, C):
    return 1 / (w * C)

# Givet
V = np.pi / 9
Itopp = 48 * 10 ** -3  # A
R = 100  # Ohm
C = 55 * 10 ** -6  # microFarad
f = 50
w = 2 * np.pi * f
faskompensering = -np.pi / 2  # negativ 90 grader för kapacitiv belastning

# Beräkna kapacitiv reaktans
xc = Xc(w, C)
print(f"Kapacitiv reaktans: {xc:.4g} Ohm")

# Tidsintervall
intervalT = np.arange(0.00, 0.02, 0.001)

# Beräkna spänningarna
ut = [Ur(R, Itopp, w, t, V) + Uc(xc, Itopp, w, t, V, faskompensering) for t in intervalT]
ur = [Ur(R, Itopp, w, t, V) for t in intervalT]
uc = [Uc(xc, Itopp, w, t, V, faskompensering) for t in intervalT]

# Skapa graf med Matplotlib
plt.figure(figsize=(10, 6))

plt.plot(intervalT, ut, label='u(t) - Total Spänning')
plt.plot(intervalT, ur, label='u_R(t) - Resistor Spänning', linestyle='--')
plt.plot(intervalT, uc, label='u_C(t) - Kondensator Spänning', linestyle=':')

plt.xlabel('Tid (s)')
plt.ylabel('Spänning (V)')
plt.title('Momentan spänning i kretsen')
plt.legend()
plt.grid()
plt.show()

# Visardiagram
ur_visare = R * Itopp
uc_visare = xc * Itopp

plt.figure(figsize=(6, 6))

plt.arrow(0, 0, ur_visare * np.cos(V), ur_visare * np.sin(V), head_width=0.02, length_includes_head=True, color='blue', label='u_R')
plt.arrow(0, 0, uc_visare * np.cos(V - np.pi/2), uc_visare * np.sin(V - np.pi/2), head_width=0.02, length_includes_head=True, color='red', label='u_C')

plt.xlim(-0.1, 0.1)
plt.ylim(-0.1, 0.1)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.title('Visardiagram')
plt.grid()
plt.show()
