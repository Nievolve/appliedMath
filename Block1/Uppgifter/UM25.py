import numpy as np

#Beräkna X

b = 4
A = 48 #grader

#x=b/np.radians(A)
x = b/np.cos(np.radians(A))
print(f"{x:.2g}")