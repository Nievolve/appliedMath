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
def ut1(Itopp, w, t,L):
    return L*Itopp*np.pi*np.cos(w*t) 

#Given information
intervalI = np.arange(1*10**-3,5*10**-3,5*10**-3/10)
w = 100*np.pi
L = 0.8 #H
constI= 10 #A

#B

Ul = [ut(intervalI, w,t)for t in intervalI]
Ylabel="Hej"
xyPlot.xyplot(Ul,len(Ul)+1,Ylabel)


#C
# L*Itopp*w*cos(w*t)


