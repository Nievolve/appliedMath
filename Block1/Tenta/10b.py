import numpy as np
import sympy as sp

# Given information
Ie1 = 4.05  # A
b1 = 15  # grader
Ie2 = 4.78  # A
b2 = 225  # grader
gammeV = 360 - (b1 + b2)

# Beräkna Ie3 med cosinussatsen
Ie3 = np.sqrt(Ie1**2 + Ie2**2 - 2 * Ie1 * Ie2 * np.cos(np.radians(gammeV)))
print(f"Ie3 = {Ie3:.3g}")

# Korrekt beräkning av cosAlfa
cosAlfa = (Ie2**2 + Ie1**2 - Ie3**2) / (2 * Ie2 * Ie1)
print(f"cos(Alfa) = {cosAlfa:.3g}")

# Beräkna vinkeln Alfa i grader
alfa_vinkel = np.degrees(np.arccos(cosAlfa))
print(f"Alfa = {alfa_vinkel:.2f} grader")

# Justering för x och b3
x = b2 - 180
b3 = 90 - x - alfa_vinkel
print(f"B3 = {b3:.2f} grader")
