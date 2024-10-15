import numpy as np

h = 12.7
b = [9.9, 9.25, 10.8, 8.05, 8.79]
a = []
p = 23.5
q = 12.7
for k in b:
    result = np.sqrt(h**2 - k**2)
    print(f"{result:.3g}")
    a.append(result)


for k in range(0,len(b)):
    hypo = np.sqrt(a[k]**2+b[k]**2)
    print("HypoTest")
    print(hypo)


x = b*q/p 

print(f"{x}")