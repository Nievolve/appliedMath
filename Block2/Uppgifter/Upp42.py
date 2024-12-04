import numpy as np
from lib import plotter
def i(t):
    return 2.5*np.sin((100*np.pi*t)+np.pi/4)
T = 1/50
timeRange=np.arange(-T,T, 0.001)
iList= [i(k) for k in timeRange]

maxIlist= max(iList)

plotter.listPlotter(iList)


for k in iList:
    print(f"{k:.2f}")