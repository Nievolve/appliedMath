# Räkneexempel 6.2
# En 100 μF kondensator uppladdas genom ett 100 Ω resistor från en 
# spänningskälla med polspänningen U = 100 V.

# a) Beräkna spänningen över kondensatorn vid följande tider. 
# Redovisa beräkningarna i värdetabellen nedan.
# Ledning: τ(tao) = R * C

# Tabell:
# t [s]         uc(t) [V]
# τ/2           ?
# τ             ?
# 2τ            ?
# 3τ            ?
# 5τ            ?

# b) Rita grafen till funktionen uc(t). Ange funktionens egenskaper.

# c) Rita grafen till funktionen i(t). Ange funktionens egenskaper.

import numpy as np
import matplotlib.pyplot as plt

C = 100 * 10**-6
R = 100
U = 100
tao = R * C

# Lista med värden som ska vara grunden för Uc
timelist = [tao / 2, tao, 2 * tao, 3 * tao, 5 * tao]
# Beräkning av Uc(t)
# Till denna uppgift så används np.exp()-funktionen för att beräkna exponentiella basen e(Euler)
returnList = [U * (1 - np.exp(-k / (R * C))) for k in timelist]

# Beräkning av I(t)
iList = [U / R * (np.exp(-k / (R * C))) for k in timelist]

# A
print("A:")
print("Uc(tao)")
for k in returnList:
    print(k)

# Skapa en canvas med flera figurer
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# B - Rita grafen för Uc(t)
ax1.plot(timelist, returnList, label="Uc(tao)")
ax1.set_xlabel("Tao")
ax1.set_ylabel("Uc(R)")
ax1.set_title("Uc(t)")
ax1.legend()

# C - Rita grafen för I(t)
print("C:")
print("I(tao)")
for k in iList:
    print(k)

ax2.plot(timelist, iList, label="I(tao)")
ax2.set_xlabel("Tao")
ax2.set_ylabel("I(A)")
ax2.set_title("I(tao)")
ax2.legend()

# Justera layouten och visa graferna
plt.tight_layout()
plt.show()
