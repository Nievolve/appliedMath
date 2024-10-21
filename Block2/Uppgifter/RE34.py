import numpy as np

def Ctopp(t):
    Ut = 325 #V
    w = 100*np.pi
    top = Ut*np.sin(w*t*10**-3)
    return top


U = 230 #V
f = 50 #Hz

Ut = 325 #V
