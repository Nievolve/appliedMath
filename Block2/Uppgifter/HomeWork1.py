from lib import timeVar as tv
import numpy as np
from lib import plotter 
f = 50
i1 = 2
phi1=np.pi / 6
i2 = 4
phi2=4*np.pi/9
i3 = tv.ItAsList(i1,f,phi1)+tv.ItAsList(i2,f,phi2)
print(i3)

plotter.listPlotter(i3)