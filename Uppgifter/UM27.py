import numpy as np

#Givet
def I():
    U = 380 #V
    Hk = 735.49875
    P2 = 3*Hk
    cosfi= 0.7
    eta = 0.8
    I = P2/(eta*U*cosfi*np.sqrt(3))
    return I

print(f"{I():.1g}")
