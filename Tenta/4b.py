# Funktion för att beräkna sidan c med hjälp av cosinussatsen och arean av en triangel
import math

def calculate_side_c(a, b, gamma):
    # Omvandla vinkeln från grader till radianer
    gamma_rad = math.radians(gamma)
    
    # Beräkna sidan c med hjälp av cosinussatsen: c = sqrt(a^2 + b^2 - 2ab * cos(gamma))
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(gamma_rad))
    
    return c

def calculate_area(a, b, gamma):
    # Omvandla vinkeln från grader till radianer
    gamma_rad = math.radians(gamma)
    
    # Beräkna arean med formeln A = 1/2 * a * b * sin(gamma)
    area = 0.5 * a * b * math.sin(gamma_rad)
    
    return area

# Parametrar
a = 4.57  # Sida a i meter
b = 12.5  # Sida b i meter
gamma = 42.5  # Vinkeln gamma i grader

# Beräkning
c = calculate_side_c(a, b, gamma)
area = calculate_area(a, b, gamma)

# Utskrift av resultatet
print(f"Längden av sidan c är {c:.2f} m")
print(f"Arean av triangeln är {area:.2f} m²")