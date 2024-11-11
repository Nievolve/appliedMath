import numpy as np
import matplotlib.pyplot as plt
from lib import recToPolForm as rp
# Räkneexempel 5.4

# a) Skriv z = 6 * (cos(30°) + j * sin(30°)) i exponentiell form.

# b) Rita talet z i det komplexa talplanet i vektorvarianten.

# c) Ange talets realdel och imaginärdel.


#Given information
thetaRad = np.deg2rad(30) # grader
absZ = 6
z = absZ*(np.cos(thetaRad)+1j*np.sin(thetaRad))



# A)

# z=|z|*e^j\theta



# B)
plt.figure()
plt.plot([0,z.real],[0,z.imag],marker="o",label=f"z={z:.2f}")


#diagrammet
plt.xlabel("Re (Real del)")
plt.ylabel("Im (Imaginär del)")
plt.axhline(0,color="grey",lw=0.5)#Ritar en horisontell linje genom origon
plt.axvline(0,color="grey",lw=0.5)#Ritar en vertical linje genom origon

plt.legend()
plt.grid()
plt.title("Räkneexempel 5.4, Komplexa tal")

# Visa
plt.show()


#C


c = rp.polToRec(absZ,np.rad2deg(thetaRad))

print(f"Reella del: {c.real:.2g}")
print(f"Imagniäradel {c.imag:.2g}")