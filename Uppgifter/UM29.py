import numpy as np

# Given information
def calc_gamma(alfa, beta):
    gamma = 180 - alfa - beta  # Beräkna vinkel gamma
    return gamma

def calc_a(c, gamma, alfa):
    # Sinuslagen: a / sin(alfa) = c / sin(gamma)
    a = (np.sin(np.radians(alfa)) * c) / np.sin(np.radians(gamma))
    return a

def calc_b(c, gamma, beta):
    # Sinuslagen: b / sin(beta) = c / sin(gamma)
    b = (np.sin(np.radians(beta)) * c) / np.sin(np.radians(gamma))
    return b

# Given angles in degrees
alfa = 35  # degrees
beta = 68  # degrees
c = 25     # meters (side c)

# Calculate gamma
gamma = calc_gamma(alfa, beta)

# Calculate the unknown sides a and b using the law of sines
a = calc_a(c, gamma, alfa)
b = calc_b(c, gamma, beta)

# Print the results
print(f"Sida a = {a:.2g} meter")
print(f"Sida b = {b:.2g} meter")
print(f"Vinkel gamma = {gamma} grader")
