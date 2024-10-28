import numpy as np
import matplotlib.pyplot as plt

# Definiera x-värden
x = np.linspace(-10, 10, 100)

# Definiera funktionen f(x) = x^2 och dess derivata f'(x) = 2x
f_x = x**2
f_prime_x = 2 * x

# Rita grafen för f(x) och f'(x)
plt.figure(figsize=(10, 6))
plt.plot(x, f_x, label="f(x) = x^2", color="blue")
plt.plot(x, f_prime_x, label="f'(x) = 2x", color="red", linestyle="--")

# Markera punkter och lutning
x_point = 3  # Ett exempelvärde
plt.scatter(x_point, x_point**2, color="blue")
plt.scatter(x_point, 2 * x_point, color="red")
plt.plot([x_point, x_point], [x_point**2, 2 * x_point], color="gray", linestyle=":")

# Märk diagrammet
plt.title("Graf av f(x) = x^2 och dess derivata f'(x) = 2x")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()



# Definiera x-värden
x = np.linspace(0, 2 * np.pi, 100)

# Definiera funktionen f(x) = sin(x)
f_x = np.sin(x)

# Steglängd för numerisk derivata
h = 1e-5

# Beräkna den numeriska derivatan
f_prime_x_approx = (np.sin(x + h) - np.sin(x)) / h

# Jämförelsefunktion: analytisk derivata f'(x) = cos(x)
f_prime_x_exact = np.cos(x)

# Rita upp både den numeriska och analytiska derivatan
plt.figure(figsize=(10, 6))
plt.plot(x, f_prime_x_approx, label="Numerisk derivata", color="green", linestyle="--")
plt.plot(x, f_prime_x_exact, label="Analytisk derivata (cos(x))", color="orange")

# Märk diagrammet
plt.title("Numerisk derivata av f(x) = sin(x) och analytisk jämförelse")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
