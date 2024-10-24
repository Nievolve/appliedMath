import numpy as np
import matplotlib as plt

def iTimes(a,t,w,v):
    i = a * np.sin(w*t+v)
    return i

W=100*np.pi

i1 = iTimes(a=2, t=0, w=W, v=0)
i2 = iTimes(a=1.5,t=0,w=W, v=np.sqrt(2)/2)

i3 = i1+i2
print(i1)
print(i2)
print(f"{i3}")


