import numpy as np
from lib import libRadDegConv as deg

# Givet 
ZMagnetude = 1500 # Ohm
ZArgument = -34.2 # Grader

# Beräkningar
fasvinkeln  = deg.degToRad(ZArgument) #
R = ZMagnetude*np.cos(fasvinkeln )
X = abs(ZMagnetude*np.sin(fasvinkeln ))
cosFactor = np.cos(fasvinkeln )

# Presentation
# A
print("A: ")
print(f"R = {R:.4g} Ohm")
# B
print("B:")
print(f"X = {X:.3g} Ohm")
# C
print("C: ")
print(f"Cosfaktorn = {cosFactor*100:.3g}%")