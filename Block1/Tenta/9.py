import numpy as np
import sympy as sp

# Given
q = 12.7
p = 23.5
b = 16.1

# Avnända lika trianglar formeln för att lösa ut närliggande katetern på den mindre triangeln.
#Lilla triangeln
a = b*q/p
# Beräkna X med pythagoras sats
x = np.sqrt(q**2-a**2)


# Resultat
print(f"X = {x:.3g} m")


# Denna har jag än inte löst
# Med facit för denna variation är rätt svar
facit = 287
H = sp.symbols("H")
Aeq = sp.Eq(facit, (p+b)/2*H)
sol = sp.solve(Aeq, H)
Oo = sol[0]

A = (p+b)/2*sol[0]
print(f"facit:")
print(f"Area = {A:.3g} m2")


