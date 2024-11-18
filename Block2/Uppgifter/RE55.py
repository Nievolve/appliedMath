from lib import complexConv as cc
import numpy as np
"""
### Räkneexempel 5.5

a) Skriv $z_1 = 1 - j$ och $z_2 = \frac{1 + j}{\sqrt{3} - j}$ i exponentiell form.

b) Beräkna. Ange svaren i rektangulär form.

   b.1) $z_1 \cdot z_2$

   b.2) $\frac{z_1}{\overline{z_2}}$

   b.3) $\frac{z_2}{z_1}$
"""

# Given information
z1 = complex(1,-1)


# 1
# A)

zPolF1 = cc.recToPol(complex(1,-1))
print(f"Det komplexa talet: {z1} blir i polar form :{zPolF1}")
zMagnetute1 = zPolF1[0]
zArgument1 = -np.pi/4
print(f"a) exponentiell form från {complex(1,-1)} är = z={zMagnetute1:.5f}*e^j{zArgument1:.2g}")
# B)
z21 = complex(1,1)
z22 = complex(np.sqrt(3),-1)
z23 = z21/z22
zPolF2 = cc.recToPol(z23)
print(zPolF2)
zMagnetute2 = zPolF2[0]
zArgument2 = np.deg2rad(zPolF2[1])
print(f"a) exponentiell form från {z21}/{z22} är = z={zMagnetute2:.2g}*e^j{zArgument2:.2g}")



# 2
b1 = z1*z23
# conjugate funktionen funkar! Den tar ett komplext tal som är skrivet i rektanulärform och gör om den till Konjugatet till Z
b2 = z1*z23.conjugate()
b3 = z23/z1

print(f"{b1:.2g}")
print(f"{b2:.2g}")
print(f"{b3:.2g}")
