import numpy as np
import matplotlib.pyplot as plt

# Definiera x-intervallet
x = np.linspace(-10, 10, 500)

# Definiera piecewise-funktionen
f_x = np.piecewise(x, [x < 0, x >= 0], [lambda x: -x, lambda x: 1-np.exp(-x)])

# Plot
plt.plot(x, f_x, label="f(x) = |x|")
plt.plot()
plt.xlabel("x")
plt.ylabel("f(x)")

plt.title("Piecewise Function in NumPy")
plt.legend()
plt.grid()
plt.show()
                                                                                                                                                                                                                                                             
