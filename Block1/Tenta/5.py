import numpy as np

def calculate_kinetic_energy(Dcm, deltaT, v, rho):
    # Omvandla till lika
    Dm = Dcm / 100  # Diameter i meter
    delta_t = deltaT * 3600  # Gör om till sekunder
    
    # beräkna
    A = np.pi * (Dm / 2) ** 2
    V = A * v * delta_t
    m = rho * V
    
    # Beräkna formeln
    Ek = 0.5 * m * v ** 2
    
    # Konvertera till kWh
    kWh = Ek / (3.6e6)
    
    return kWh

# Given information
D = 457 #cm
deltaT = 34.4 #h
v = 14.8 #m/s
rho = 1.29 #kg/m3

EkkWh = calculate_kinetic_energy(D, deltaT, v, rho)
print(f"Den teoretiska kinetiska energin är: {EkkWh:.2f} kWh")