# Bilder nedan visar grafen till sinus- och cosinusfunktion
# för vinklar i intervallet 0 <= x <= 2π rad. Använd graferna för att
# få närmevärde till följande trigonometriska ekvationer i det
# intervallet. Ange även lösningar i vinkelmått grader.

# a) sin(x) = 0.6
# b) sin(x) = -0.9
# c) cos(x) = 0.6
# d) cos(x) = -0.8
import numpy as np
import matplotlib.pyplot as plt

def sinX(value):
    if value < -1 or value > 1:
        raise ValueError("Sinusvärdet måste vara mellan -1 och 1")
    
    # Första lösningen (positivt värde i första kvadranten)
    x1 = np.arcsin(value)
    # Andra lösningen (positivt värde i andra kvadranten)
    x2 = np.pi - x1
    
    return x1, x2
def cosX(value):
    if value < -1 or value > 1:
        raise ValueError("Cosinusvärdet måste vara mellan -1 och 1")
    
    # Första lösningen (positivt värde i första kvadranten)
    x1 = np.arccos(value)
    # Andra lösningen (negativt värde i fjärde kvadranten)
    x2 = 2 * np.pi - x1
    
    return x1, x2
# SÖKT
sin_value = 0.6
negativeSin = -0.9
negativeCos = -0.8

try:
    x1, x2 = sinX(sin_value)
    print(f"Lösningarna för sin(x) = {sin_value} i intervallet [0, 2π] är:")
    print(f"x1 ≈ {x1:.2f} rad")
    print(f"x2 ≈ {x2:.2f} rad")
except ValueError as e:
    print(e)
try:
    x1, x2 = sinX(negativeSin)
    print(f"Negative SIN, -0.9")
    print(f"x1 ≈ {x1:.2f} rad")
    print(f"x2 ≈ {x2:.2f} rad")
except ValueError as e:
    print(e)

try:
    x1, x2 = cosX(negativeCos)
    print(f"NEGATIVE COS, -0.8")
    print(f"x1 ≈ {x1:.2f} rad")
    print(f"x2 ≈ {x2:.2f} rad")
except ValueError as e:
    print(e)
try:
    x1, x2 = cosX(sin_value)
    print(f"SIN VALUE 0.6")
    print(f"x1 ≈ {x1:.2f} rad")
    print(f"x2 ≈ {x2:.2f} rad")
except ValueError as e:
    print(e)
# PLOTTER
x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)

plt.plot(x, y, label='sin(x)')
plt.axhline(y=sin_value, color='r', linestyle='--', label=f'sin(x) = {sin_value}')
plt.scatter([x1, x2], [sin_value, sin_value], color='b', zorder=5, label='Lösningar')

plt.xlabel('x [radianer]')
plt.ylabel('sin(x)')
plt.title('Graf för sin(x) och lösningar för sin(x) = 0.6')
plt.legend()
plt.grid(True)
plt.show()
