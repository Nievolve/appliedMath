import numpy as np
import cmath as cm

# Z = R+j(Xl-Xc)


R1= 20
Xl1 = 10
R2 = 10
Xl2 = 5
Xc2 = 1


#Rektangulär form
z1=complex(R1,Xl1)
z2=complex(R2, Xl2-Xc2)
ztot=complex(z1+z2)

print(ztot)



#Polar form
zabs = abs(ztot)
magnitude=np.sqrt((R1+R2)**2+(Xl1+Xl2-Xc2)**2)
print(magnitude)

print(zabs)

rad = cm.phase(ztot)

print(np.rad2deg(rad))
