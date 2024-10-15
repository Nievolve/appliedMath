import numpy as np
# Given
q = 12.7
p = 23.5
b = 16.1

# Avnända lika trianglar formeln för att lösa ut närliggande katetern på den mindre triangeln.
#Lilla triangeln

a = b*q/p
print(a)
helaH = q+p
helaA = 8.7+b
print(helaH, helaA)
x = np.sqrt(q**2-a**2)

A = (p+b)/2
print(A)

# Denna har jag än inte löst