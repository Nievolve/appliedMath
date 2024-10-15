import numpy as np

h = 12.7
b = 8.79
a = 9.17
p = 23.5
q = 12.7
base = 16.1


x = base*q/p
print(f"X = {x:3g}")
print(a)
print(f"{x:.3g}")


helaH= q +p
helaA = base+a

helaB= np.sqrt(helaH**2-helaA**2)


print(f"BHöjden = {helaB:.4g}")

traArea = helaB*(p+base)/2

print(f"Area = {traArea:.3g}")