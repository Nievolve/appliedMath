import cmath

# r = absolutbelopp (magnituden)
# theta = vinkeln (argumentet) i radianer
r = 5
theta = cmath.pi / 4  # 45 grader = π/4 radianer

# Komplext tal i exponentiell form
z = r * cmath.exp(1j * theta)

# Utskrift
print(f"Komplex tal i exponentiell form: {z}")
print(f"Reell del: {z.real}")
print(f"Imaginär del: {z.imag}")
