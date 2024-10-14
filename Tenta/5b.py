# Funktion för att beräkna den teoretiska kinetiska energin för ett vindkraftverk och tillförd effekt för ventilationssystem
import math

def calculate_kinetic_energy(diameter, time_interval, velocity, density):
    # Omvandla diameter från cm till meter
    diameter_m = diameter / 100
    
    # Beräkna volymen av luftcylindern V = A * (v * Δt)
    area = math.pi * (diameter_m / 2) ** 2
    volume = area * velocity * time_interval * 3600  # Omvandla timmar till sekunder
    
    # Beräkna massan m = ρ * V
    mass = density * volume
    
    # Beräkna den kinetiska energin Ek = (m * v^2) / 2
    kinetic_energy = (mass * velocity ** 2) / 2
    
    return kinetic_energy

def calculate_power(q, delta_p, eta_total):
    # Beräkna tillförd effekt enligt formeln P_tillförd = (q * Δp) / η_tot
    power = (q * delta_p) / eta_total
    return power

# Parametrar för kinetisk energi
diameter = 457  # Diameter i cm
time_interval = 34.4  # Tidsintervall i timmar
velocity = 14.8  # Vindhastighet i m/s
density = 1.29  # Densitet i kg/m^3

# Beräkning av kinetisk energi
kinetic_energy = calculate_kinetic_energy(diameter, time_interval, velocity, density)

# Omvandla energin från joule till kilowattimmar (1 kWh = 3.6e6 J)
kinetic_energy_kwh = kinetic_energy / 3.6e6

# Utskrift av resultatet för kinetisk energi
print(f"Den teoretiska kinetiska energin är {kinetic_energy_kwh:.2f} kWh")

# Parametrar för ventilationssystem
delta_p = 100  # Tryckdifferens i Pa (exempelvärde)
q = 0.5  # Volymflöde i m^3/s (exempelvärde)
eta_total = 0.76  # Fläktens totala verkningsgrad (exempelvärde)

# Beräkning av tillförd effekt
power = calculate_power(q, delta_p, eta_total)

# Utskrift av resultatet för tillförd effekt
print(f"Den tillförda effekten är {power:.2f} W")