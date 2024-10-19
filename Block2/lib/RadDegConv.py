import numpy as np

def rad_to_deg(rad):
    """
    Konvertera radianer till grader.
    
    :param rad: Värdet i radianer
    :return: Värdet i grader
    """
    return (180 / np.pi) * rad

def deg_to_rad(deg):
    """
    Konvertera grader till radianer.
    
    :param deg: Värdet i grader
    :return: Värdet i radianer
    """
    return (np.pi / 180) * deg

# Testa konverteringar mellan radianer och grader
rad = float(input("Ange värdet i radianer som ska konverteras till grader: "))
deg = float(input("Ange värdet i grader som ska konverteras till radianer: "))

print(f"{rad} radianer är lika med {rad_to_deg(rad)} grader.")
print(f"{deg} grader är lika med {deg_to_rad(deg)} radianer.")
