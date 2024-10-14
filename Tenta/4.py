import numpy as np


a = 4.57 #m
b = 12.5 #m
gamma = 42.5 # grader
cos = np.radians(gamma)
c = np.sqrt(a**2+b**2-2*a*b*np.cos(cos))
print (f"c= {c:.3g}")


area = a*b*np.sin(cos)/2
print(f"Area är {area:.3g}")


