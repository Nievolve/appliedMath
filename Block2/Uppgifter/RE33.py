import numpy as np
from fractions import Fraction
# E3.1 : sin(2x) = 2 * sin(x) * cos(x)
a = 3
o = 1
h = np.sqrt(a**2 + o**2)  # Hypotenusan 

x = o / h  # Vinkel SIN
y = a / h  # VInkel COS
 
bevisSin = 2 * round(np.sin(x) * np.cos(x),1)  # Beräkna sin(2x) med formel
bevisCos =  round((np.sin(y)**2)-(np.cos(y))**2,)



# Exempel föra om decimaltal till bråk!

fraction = Fraction(bevisSin).limit_denominator()
print(fraction)
fraction = Fraction(bevisCos).limit_denominator()
print(fraction)