import sympy as sp

# Definiera symboler
L = sp.Symbol('L')  # Induktans
C = 80e-12  # Kapacitans i farad
foa = 7e6  # Resonansfrekvens i Hz
pi = sp.pi  # Pi från SymPy

# Ställ upp ekvationen för resonansfrekvens
eq = sp.Eq(foa, 1 / (2 * pi * sp.sqrt(L * C)))

# Lös ekvationen för L
solution = sp.solve(eq, L)
solutionone = float(solution[0])
# Visa lösningen
print(solution)
print(type(solution))
print(f"{solutionone:.2g}")