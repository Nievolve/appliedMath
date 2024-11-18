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
from lib import complexConv as cc
from fractions import Fraction

# Given information
R = 100 #Ohm
L = 0.250
#Case1
tildeU1Magnetute = 230
tildeU1argument = 0
freqvensCase1 = 50.0 #Hz
#Case2
tildeU2Magnetute = 110
tildeU2Argument = 0
freqvensCase2 = 60.0 #Hz

# Sökt information
# A)
z = "?"
AbsZ = "?"
phi = "?"
# B)
tildeI="?"
Ie="?"
faskonstantBeta = "?"
# C)



#---
# Beräkningar
#---
## Case 1
print("CASE1")
componentOne = R #+j(Xl=0-Xc=0)
# Impedans Z för KomponentEtt är endast R då det är en ren resistiv belastning utan induktion eller kapacitet

# Komponent Två
componentTwo = complex(R,2*np.pi*freqvensCase1*L)
# Komponenten är en induktiv. Läser in samma formel från den förra komponenten (z=R+(Xl-Xc)j

# Beräknar ersättnings impedansen (totala impedansen)
completeImpedans = ((1/componentOne)+(1/componentTwo))**-1
# Utskriv i rektangulärform
print(f"Rektangulär form : {completeImpedans:.3g}")
# Lägger expoentiella formen i en list (Index 0= absolute ,1= theta)
expoList = cc.rectoExp(completeImpedans)
# Skriv om decimaltalet till bråk
thetaRad = Fraction(expoList[1]).limit_denominator(1000)
# Utskrift i exponentiell form
print(f"Exponentiell form : {expoList[0]:.3g}*e^{expoList[1]:.3g}")
## Case 1 END

## Case 2
print("CASE2")

componentOne = R #+j(Xl=0-Xc=0)
# Komponent Två
componentTwo = complex(R,2*np.pi*freqvensCase2*L)
# Komponenten är en induktiv. Läser in samma formel från den förra komponenten (z=R+(Xl-Xc)j
completeImpedans = ((1/componentOne)+(1/componentTwo))**-1
# Beräknar ersättnings impedansen (totala impedansen)
print(f"Rektangulär form : {completeImpedans:.3g}")
# Lägger expoentiella formen i en list (Index 0= absolute ,1= theta)
expoList = cc.rectoExp(completeImpedans)
# Skriv om decimaltalet till bråk
thetaRad = Fraction(expoList[1]).limit_denominator(1000)
# Utskrift i exponentiell form
print(f"Exponentiell form : {expoList[0]:.3g}*e^{expoList[1]:.3g}")
## Case 2 END



