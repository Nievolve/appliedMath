import numpy as np
import sympy as sp

def q(t):
    return -11*np.exp(-0.0611*t)+11

# Given information
t_1 = 9.15  # Tidpunkt i sekunder
h = 0.02 #sekunder
#Sökt
# q(9.15)
# Ledning : q(t)=-11*e^(-0.0611*t)+11

# A 
momentanQ=q(t_1) #mAs

# B
lutandeQ = t_1+h
I = (q(lutandeQ)-q(t_1))/h # mA



# Presentation
print(f"q vid tidpunken {t_1}s = {momentanQ:.2g} mAs")
print(f"Kondensatorström vid {h*10**3}ms = {I*10**3:.3g} microA")
