import numpy as np

def calculate_resistance(L, D, r):
    # Formel för att få fram Area i meter**2
    A = (np.pi * D**2) / 4
    # Beräkna resistansen i mOhm
    R = (r * L) / A
    return R

# Given information
r = 2.71e-8  # Resistivitet i Ωm
L = 2179e-3  # Längd i meter (2179 mm omvandlat till meter)
D = 1.95e-3  # Diameter i meter (1.95 mm omvandlat till meter)

# Beräkning
resistance = calculate_resistance(L, D, r)*10**3

print(f"Resistansen är {resistance:.3g} mOhm")