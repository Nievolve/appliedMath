# Räkneexempel 3.7
# Genom en spole med induktansen 0,8 H går en ström. Beräkna den inducerade spänningen över spolen då strömmen:
# a) är konstant 10 A
# b) ökar linjärt från 0 till 0,5 A på 10 ms
# c) är en sinusformad ström i(t) = 0,75 * sin(100πt) [A]

import numpy as np
import matplotlib.pyplot as plt

# Given information
L = 0.8  # Induktans i Henry (H)

# a) Spänningen över spolen då strömmen är konstant i(t) = 10 A
def induced_voltage_constant_current(L, I):
    # Om strömmen är konstant är derivatan 0, så spänningen är 0
    return 0

I_const = 10  # A
U_a = induced_voltage_constant_current(L, I_const)
print(f"a) Spänningen över spolen är {U_a} V då strömmen är konstant 10 A.")

# b) Spänningen över spolen då strömmen ökar linjärt från 0 A till 0,5 A på 10 ms
def induced_voltage_linear_current(L, dI, dt):
    return L * (dI / dt)

dI = 0.5  # A
dt = 10e-3  # s (10 ms)
U_b = induced_voltage_linear_current(L, dI, dt)
print(f"b) Spänningen över spolen är {U_b} V då strömmen ökar linjärt från 0 A till 0,5 A på 10 ms.")

# c) Spänningen över spolen då strömmen är en sinusformad funktion i(t) = 0,75 * sin(100πt) [A]
def induced_voltage_sinusoidal_current(L, I_peak, omega, t):
    # Derivera strömmen: di/dt = I_peak * omega * cos(omega * t)
    return L * I_peak * omega * np.cos(omega * t)

I_peak = 0.75  # A
omega = 100 * np.pi  # rad/s
t = np.linspace(0, 0.1, 1000)  # Tid från 0 till 0,1 s

U_c = induced_voltage_sinusoidal_current(L, I_peak, omega, t)

# Plotta spänningen över tiden
plt.plot(t, U_c)
plt.title("Inducerad spänning över spole vid sinusformad ström")
plt.xlabel("Tid (s)")
plt.ylabel("Spänning (V)")
plt.grid()
plt.show()
