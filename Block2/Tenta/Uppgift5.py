import numpy as np
import matplotlib.pyplot as plt

# Funktion för att beräkna spänning över impedans
def Ux(I_tilde, Z):
    return I_tilde * Z

# Given information
ITilde = 80e-3 * np.exp(1j * np.radians(60))  # ITopp
Z1 = 286 + 48j  # rektangulär form (R+(Xl-Xc))
Z2 = 110 - 77j  # rektangulär form
Z3 = 197 + 15j  # rektangulär form

# Beräkna spänningar
U1 = Ux(ITilde, Z1)  # 
U2 = Ux(ITilde, Z2)  # S
U3 = Ux(ITilde, Z3)  # Spänning över Z3

# Tidsram -20ms -- 20ms
time = np.linspace(-0.02, 0.02, 1000)

# Amplituder och faser från spänningarna
U1Magenetute, U1Argument = np.abs(U1), np.angle(U1)
U2Magenetute, U2Argument = np.abs(U2), np.angle(U2)
U3Magenetute, U3Argument = np.abs(U3), np.angle(U3)

# Skapar signaler
U1Signal = U1Magenetute * np.sin(2 * np.pi * 50 * time + U1Argument)
U2Signal = U2Magenetute * np.sin(2 * np.pi * 50 * time + U2Argument)
U3Signal = U3Magenetute * np.sin(2 * np.pi * 50 * time + U3Argument)

# Plotter
plt.figure(figsize=(12, 8))
plt.plot(time * 1000, U1Signal, label="U1 över Z1")
plt.plot(time * 1000, U2Signal, label="U2 över Z2", linestyle="--")
plt.plot(time * 1000, U3Signal, label="U3 över Z3", linestyle=":")

# Plotter
plt.title("Oscilloskopssignaler för Z1, Z2 och Z3", fontsize=14)
plt.xlabel("Tid (ms)", fontsize=12)
plt.ylabel("Spänning (V)", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()
