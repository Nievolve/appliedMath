import numpy as np

def is_trigonometric_identity(x, y, tolerance=1e-6):
    """
    Kontrollera om ett par (x, y) uppfyller trigonometriska identiteten sin^2 + cos^2 = 1
    med en given tolerans för att hantera avrundningsfel.
    
    :param x: Värdet på sin(θ)
    :param y: Värdet på cos(θ)
    :param tolerance: Tolerans för felmarginal (standard är 1e-6)
    :return: True om identiteten är uppfylld, annars False
    """
    result = np.square(x) + np.square(y)
    return np.isclose(result, 1, atol=tolerance)

# Testa programmet
x_value = float(input("Ange värdet för sin(θ): "))
y_value = float(input("Ange värdet för cos(θ): "))

if is_trigonometric_identity(x_value, y_value):
    print(f"Värdena ({x_value}, {y_value}) uppfyller trigonometriska identiteten.")
else:
    print(f"Värdena ({x_value}, {y_value}) uppfyller INTE trigonometriska identiteten.")


if __name__ == "__main__":
    pass