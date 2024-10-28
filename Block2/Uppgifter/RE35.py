import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
def Icalc(itopp, t, w, V):
    return itopp * np.sin(w * t + V)
def top(x):
    y = max(x)
    return y
#Givet
w = 100 * np.pi

interval = np.arange(0, 0.1, 0.001)  # Från 0 till 0.1 sekunder med steget 0.001

# Beräkna strömvärden för varje tidpunkt i intervallet
I1Graf = [Icalc(itopp=2, t=k, w=w, V=0) for k in interval]
I2Graf = [Icalc(itopp=1.5, t=k, w=w, V=np.sqrt(2)/2) for k in interval]
I3Graf = [Icalc(itopp=1.5, t=k, w=w, V=np.sqrt(2)/2)+Icalc(itopp=2, t=k, w=w, V=0)for k in interval]

print("Max är: ",top(I3Graf))
# Sympy
beta = sp.symbols("beta")
eqI3 = sp.Eq(1.1, 3.2*sp.sin(w*0+beta))
solve = sp.solve(eqI3, beta)
print(solve)


# Plotta resultaten
plt.plot(interval, I1Graf, label="I1")
plt.plot(interval, I2Graf, label="I2")
plt.plot(interval, I3Graf, label="I3")
# Sätt etiketter för axlarna
plt.xlabel("Tid (sekunder)")
plt.ylabel("Ström (A)")

# Sätt en titel
plt.title("Sinusformad Ström över Tid")

# Aktivera rutnät och legend
plt.grid(True)
plt.legend()

# Visa grafen
plt.show()


