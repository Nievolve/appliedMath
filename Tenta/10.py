import numpy as np
import sympy as sp

#Given information
Ie1 = 4.05 #A
b1 = 15 #grader
Ie2 = 4.78 #A
b2 = 225
gammeV = 360-(b1+b2)
Ie3 =np.sqrt(Ie1**2+Ie2**2-2*Ie1*Ie2*np.cos(np.radians(gammeV)))

print(f"Ie3= {Ie3:.3g}")
cosAlfa = Ie2**2+Ie1**2-Ie3**2/(2*Ie2*Ie1)
print(cosAlfa)
x=b2-180
print(x)
b3 = 90-x-cosAlfa
print(b3)


allaV = 180-gammeV


def calculate_cosine_law_angle(a, b, c):
    # Definiera variabler
    A, B, C = sp.symbols('A B C')
    
    # Cosinussatsen: c**2 = a**2 + b**2 - 2*a*b*cos(C)
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    
    # Beräkna vinkeln C i radianer
    C_radianer = sp.acos(cos_C)
    
    # Konvertera radianer till grader
    C_grader = sp.deg(C_radianer)
    
    return C_radianer, C_grader

# Exempelvärden
sid_a = Ie3
sid_b = Ie2
sid_c = Ie1

# Beräkna vinkeln
vinkel_radianer, vinkel_grader = calculate_cosine_law_angle(sid_a, sid_b, sid_c)

# Skriv ut resultat
print(f"Vinkeln i radianer: {vinkel_radianer:.2f}")
print(f"Vinkeln i grader: {vinkel_grader:.2f}")


alfaVin= np.sin(gammeV)*Ie3/Ie3
print(f"Alfa = {np.degrees(alfaVin):.3g}")

b3= 90-45-np.degrees(alfaVin)
print(np.degrees(alfaVin))
print(b3)