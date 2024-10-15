import numpy as np

# Vinklar i grader
grader = [30, 45, 60, 55]

# Beräkna sin, cos, och tan för varje vinkel
print("Sinusvärden:")
sinVinklar =[]
for vinkel in grader:
    print(f"sin({vinkel}°) = {np.sin(np.radians(vinkel)):.2g}")
    sinVinklar.append(np.sin(np.radians(vinkel)))

print("\nCosinusvärden:")
cosVinklar =[]
for vinkel in grader:
    print(f"cos({vinkel}°) = {np.cos(np.radians(vinkel)):.2g}")
    cosVinklar.append(np.cos(np.radians(vinkel)))

print("\nTangensvärden:")
tanVinklar = []
for vinkel in grader:
    print(f"tan({vinkel}°) = {np.tan(np.radians(vinkel)):.2g}")
    tanVinklar.append(np.tan(np.radians(vinkel)))

