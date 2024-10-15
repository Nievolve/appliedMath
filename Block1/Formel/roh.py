import matplotlib.pyplot as plt

# Funktion för att beräkna Um
def Um(Ue, Ie, L, A, rå):
    return Ue - (2 * rå * L / A) * Ie

# Konstanter
Ue = 230  # Spänning i Volt
Ie = 5.0  # Ström i Ampere
A = 2.5e-6  # Fast tvärsnittsarea (2.5 mm²)
L = 100  # Fast längd på kabeln i meter

# Lista med olika ledarresistiviteter (rå) i ohm-meter för olika material
rå_values = [1.59e-8, 1.68e-8, 2.44e-8, 5.60e-8, 9.71e-8]  # Resistivitet för olika material

# Beräkna Um för olika resistiviteter
Um_values_rå = [Um(Ue, Ie, L, A, rå) for rå in rå_values]

# Skapa en graf för spänning beroende på ledarresistivitet
plt.plot(rå_values, Um_values_rå, label="Spänning över kabel (Um)")
plt.xlabel('Ledarresistivitet (Ohm-meter)')
plt.ylabel('Spänning (V)')
plt.title('Spänning (Um) som funktion av ledarresistivitet')
plt.grid(True)
plt.legend()
plt.show()
