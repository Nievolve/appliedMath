import numpy as np

def itime(itopp,f,beta,t):
    i=itopp*np.sin(2*np.pi*f*t+np.deg2rad(beta))
    return i

# Given information
iTopp = 0.05
f =60
beta = 134
# Variabel
t = 0.0015
#Sökt information
result = itime(iTopp,f,beta,t)
print(f"Vid {t*10**3} ms är i= {result*10**3:.3g} mA")