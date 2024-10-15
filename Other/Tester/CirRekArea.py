import numpy as np

# Teorin, enligt youtube Short, är att en cirkel och rektangel med samma area har lika mellan:
# radie=höjd
# omkrets = bredd

testvalue = 12
radie = testvalue
height = testvalue


circelCircumfernce = 2*np.pi*radie
circleArea = np.pi*radie**2
print(f"Cirkel omkrets = {circelCircumfernce:.1f}. Cirkel Area = {circleArea:.1f}")

base = circelCircumfernce
rekArea = height*base/2
print(f"Rektangel area = {rekArea:.1f}")
if rekArea == circleArea:
    print("Korrekt")
else:
    print("Inte")