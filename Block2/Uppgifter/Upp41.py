import numpy as np
from lib import plotter

def u(t):
    return 85*np.sin(628*t)

T = 100*np.pi
w = 2*np.pi/T

aRange= np.arange(-20,20,0.1)
uList = [u(k) for k in aRange]
maxUList = max(uList)
print(f"U Topp = {maxUList}")

Ue=max(uList)/np.sqrt(2)

print(f"Ue = {Ue} V")
plotter.listPlotter(uList)