import cmath as cm
import numpy as np


magnitute = 2
argument = 30 #grader
argumentRad = np.deg2rad(argument)
z = cm.rect(magnitute,argumentRad)

print(z)
print(z.real)
print(z.imag)