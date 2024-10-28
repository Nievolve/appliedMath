#Räkneexempel 3.7
#Genom en spole med induktansen 0,8 H går en ström. Beräkna den inducerade spänningen över spolen då strömmen:
#a) är konstant 10 A
#b) ökar linjärt från 0 till 0,5 A på 10 ms
#c) är en sinusformad ström i(t)=0,75⋅sin⁡(100πt) [A]

#Given information:

#    Induktans, L=0,8

#Sökt information:

#    a) Spänningen över spolen då strömmen är konstant i(t)=10 
#    b) Spänningen över spolen då strömmen ökar linjärt från 0 A till 0,5 A på 10ms
#    c) Spänningen över spolen då strömmen är en sinusformad funktion i(t)=0,75⋅sin⁡(100πt) [A]

import numpy as np
from lib import xyPlot

def ut(Itopp,w,t):
    return Itopp*np.sin(w*t)

a = 0.005/10
intervalI = np.arange(0.001,0.005,a)
w = 100*np.pi


constI= 10 #A

aU=constI*np.sin(w*0)

#B

Ul = [ut(intervalI, w,t)for t in intervalI]
Ylabel="Hej"
xyPlot.xyplot(Ul,len(Ul)+1,Ylabel)