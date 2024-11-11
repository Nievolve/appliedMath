# Komponenter:
# - R = 100 Ω
# - L = 0,250 H

# Uppgifter:
# a) Beräkna den totala komplexa impedansen i kretsen. Skriv den i rektangulär form och i exponential form.
# b) Beräkna den komplexa strömmen i polär form och i exponential form.
# c) Rita grafen till funktionerna i(t) och u(t).

# Fall I:
#   U~ = 230 ∠ 0°; f = 50.0 Hz
# Fall II:
#   U~ = 110 ∠ 0°; f = 60.0 Hz

# Lösning

# Definera

# Givet:
# - Elektrisk krets
# - Komponenter: Två impedanser i parallellkoppling med en växelspänningskälla.
#   - R = 100 Ω
#   - L = 0,250 H

# Sökt:
# a) Z = ? ⇒ |Z| = ? och φ
# b) I~ = ? ⇒ I_e = ? och faskonstanten β = ?
# c) Rita grafer till funktionerna i(t) och u(t)
import numpy as np
import cmath as cm
import matplotlib as plt

# Given information
R = 100 #Ohm
L = 0.250
#Case1
tildeU1Magnetute = 230
tildeU1argument = 0
f1 = 50.0 #Hz
#Case2
tildeU2Magnetute = 110
tildeU2Argument = 0
f2 = 60.0 #Hz

# Sökt information
# A)
z = "?"
AbsZ = "?"
phi = "?"
# B)
tildeI="?"
Ie="?"
faskonstantBeta = "?"


z1 = R #+j(0-0)
z2 = complex(R,2*np.pi*f1*L)
zp1 = ((1/z1)+(1/z2))**-1
zc1 = R
zc2 =complex(R,2*np.pi*f2*L)
zpc2 =((1/zc1)+(1/zc2))**-1
print(f"{zp1:.3g}")
print(f"{zpc2:.3g}")