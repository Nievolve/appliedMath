import numpy as np
import matplotlib.pyplot as plt

# Given values
Q = 62  # Var (Reactive power)
S = 95  # VA (Apparent power)

# Calculate P (Real power) using Pythagorean theorem
P = np.sqrt(S**2 - Q**2)

# Create the plot
plt.figure()
plt.title('Effekttriangel')

# Plot the triangle sides
plt.plot([0, P], [0, 0], label="P (Verklig effekt)")  # P as horizontal line
plt.plot([P, P], [0, Q], label="Q (Reaktiv effekt)")  # Q as vertical line
plt.plot([0, P], [0, Q], label="S (Skeneffekt)")      # S as hypotenuse

# Label the sides
plt.text(P/2, -2, 'P', horizontalalignment='center', fontsize=12)
plt.text(P + 2, Q/2, 'Q', verticalalignment='center', fontsize=12)
plt.text(P/2, Q/2, 'S', horizontalalignment='center', verticalalignment='center', fontsize=12)

# Set limits and aspect ratio for better visualization
plt.xlim(0, S)
plt.ylim(0, Q + 10)
plt.gca().set_aspect('equal')

# Add grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
