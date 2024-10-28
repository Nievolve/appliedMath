import numpy as np
from lib import xyPlot as xy

exp = []
for k in range(1,100):
    result = 0.25 * sum([ell + 300 * np.power(2, ell / 7) for ell in range(1, k)])
    #result = 3+9*k*np.sqrt(k)
    exp.append(result)

xy.xyplot(y=exp,L = len(exp)+1, yLabel= "TESTER")

