# Förekommer i
# RE 3.1


import numpy as np
import matplotlib.pyplot as plt
def plot(x1,x2,value):
    # PLOTTER
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x)

    plt.plot(x, y, label='PLACEHOLDER(x)')
    plt.axhline(y=value, color='r', linestyle='--', label=f'PLACEHOLDER(x) = {value}')
    plt.scatter([x1, x2], [value, value], color='b', zorder=5, label='Lösningar')

    plt.xlabel('PLACEHOLDER [radianer]')
    plt.ylabel('PLACEHOLDER(x)')
    plt.title('PLACEHOLDER')
    plt.legend()
    plt.grid(True)
    plt.show()

def sinX(value):
    if value < -1 or value > 1:
        raise ValueError("Sinusvärdet måste vara mellan -1 och 1")
    
    # Första lösningen (positivt värde i första kvadranten)
    x1 = np.arcsin(value)
    # Andra lösningen (positivt värde i andra kvadranten)
    x2 = np.pi - x1

    # PLOTTER Funktion
    plot(x1,x2,value)
    print(x1,x2)
    return x1, x2


def cosX(value):
    if value < -1 or value > 1:
        raise ValueError("Cosinusvärdet måste vara mellan -1 och 1")
    
    # Första lösningen (positivt värde i första kvadranten)
    x1 = np.arccos(value)
    # Andra lösningen (negativt värde i fjärde kvadranten)
    x2 = 2 * np.pi - x1
    plot(x1,x2,value)
    print(x1,x2)
    return x1, x2





if __name__ == "__main__":
    sin_value = 0.6
    cos_value = 0.6

    try:
        x1, x2 = sinX(sin_value)
        print(f"Lösningarna för sin(x) = {sin_value} i intervallet [0, 2π] är:")
        print(f"x1 ≈ {x1:.2f} rad")
        print(f"x2 ≈ {x2:.2f} rad")
    except ValueError as e:
        print(e)
    try:
        x1, x2 = cosX(sin_value)
        print(f"Lösningarna för sin(x) = {sin_value} i intervallet [0, 2π] är:")
        print(f"x1 ≈ {x1:.2f} rad")
        print(f"x2 ≈ {x2:.2f} rad")
    except ValueError as e:
        print(e)

