import numpy as np

def radToDeg(rad):
    """
    Konvertera radianer till grader.
    """
    return (180 / np.pi) * rad

def degToRad(deg):
    """
    Konvertera grader till radianer.
    """
    return (np.pi / 180) * deg
if __name__ == "__main__":
# Testa konverteringar mellan radianer och grader
    rad = float(input("Ange värdet i radianer som ska konverteras till grader: "))
    deg = float(input("Ange värdet i grader som ska konverteras till radianer: "))

    print(f"{rad} radianer är lika med {radToDeg(rad)} grader.")
    print(f"{deg} grader är lika med {degToRad(deg)} radianer.")
