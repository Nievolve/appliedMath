import numpy as np

p = 23.5
q = 12.7
b = 16.1
x = 9.25
a = np.sqrt(q**2-x**2)
print(f"X = {x:.3g}")

print(f"{a:.3g}")

helaH = q+p
helaA = a + b
helaO = np.sqrt(helaH**2-helaA**2)
h = p*x/b
print(f"Höjden är enligt: {h:.3g}")
# print(f"BHöjden = {helaO:.4g}")

# Korrigera areaberäkningen för trapetsen
traArea = (b + p) * h / 2

print(f"Area = {traArea:.3g}")

