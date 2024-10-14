# Funktion för att beräkna resistansen
import math

def calculate_resistance(length, diameter, resistivity):
    # Beräkna tvärsnittsarean med formeln A = (π * D^2) / 4
    area = (math.pi * diameter**2) / 4
    
    # Beräkna resistansen med formeln R = (ρ * L) / A
    resistance = (resistivity * length) / area
    
    return resistance

# Parametrar
resistivity = 2.71e-8  # Resistivitet i Ωm
length = 2179e-3  # Längd i meter (2179 mm omvandlat till meter)
diameter = 1.95e-3  # Diameter i meter (1.95 mm omvandlat till meter)

# Beräkning
resistance = calculate_resistance(length, diameter, resistivity)

# Utskrift av resultatet
print(f"Resistansen är {resistance:.5f} Ω")