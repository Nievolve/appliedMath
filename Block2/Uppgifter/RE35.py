import numpy as np
import matplotlib.pyplot as plt

# Funktion för att beräkna i(t)
def iTimes(a, t, w, v):
    i = a * np.sin(w * t + v)
    return i

# Frekvensen W
W = 100 * np.pi

# Tidsarray för att plotta grafen
t = np.linspace(0, 10, 1000)

# Beräknar strömmarna
i1 = iTimes(a=2, t=t, w=W, v=0)
i2 = iTimes(a=1.5, t=t, w=W, v=np.sqrt(2)/2)

# Summa av de två strömmarna
i3 = i1 + i2

# Utskrift av värdena vid t=1 och t=2
print(iTimes(a=2, t=0, w=W, v=0))  # i1 vid t=1
print(iTimes(a=1.5, t=0, w=W, v=np.sqrt(2)/2))  # i2 vid t=2
print(f"{iTimes(a=2, t=0, w=W, v=0) + iTimes(a=1.5, t=2, w=W, v=np.sqrt(2)/2)}")  # i3 vid t=1 och t=2

# Plotta strömmarna
plt.figure()
plt.plot(t, i1, label='i1(t)')
plt.plot(t, i2, label='i2(t)')
plt.plot(t, i3, label='i3(t) = i1(t) + i2(t)')
plt.xlabel('Tid (s)')
plt.ylabel('Ström (A)')
plt.title('Strömmar som funktion av tid')
plt.legend()
plt.grid(True)
plt.show()
