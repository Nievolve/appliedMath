import numpy as np

#Information
#0=Iu-I1+I2
#Faskonstanter; b1,b2,b3

#Given information
Ie1 = 473*10**-3 #A
b1 = 73.6 #grader
Ie2 = 319*10**-3 #A
b2 = 19.0 #graderm tredje kvadraten
b1b2=b1+b2
print(b1b2)
I1I2Vinkel = (360 - 2*b1b2) /2
print(I1I2Vinkel)
deltaVinkel = 180-b1-I1I2Vinkel
print(deltaVinkel)

#Sökt
Ie3 =np.sqrt(Ie1**2+Ie2**2-2*Ie1*Ie2*np.cos(np.radians(I1I2Vinkel)))
print(f"{Ie3*10**3:.3g}")
b3 = ""