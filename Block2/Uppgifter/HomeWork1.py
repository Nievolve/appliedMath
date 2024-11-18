import numpy as np

from lib import timeVar as tv
from lib import plotter


# Givet
f = 50
# i1
i1 = 2
phi1=np.pi / 6
# i2

i2 = 4
phi2=4*np.pi/9
# Sökt
# i3
timeRange = np.arange(-1/f,1/f,0.001)
i3 = [tv.IasOne(i1,f,k,phi1)+tv.IasOne(i2,f,k,phi2)for k in timeRange]
print(max(i3))
plotter.listPlotter(i3)