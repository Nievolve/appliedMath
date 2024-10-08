import sympy as sp

# Definiera symbolen x
x = sp.Symbol("x")

# Definiera ekvationen
eqa = sp.Eq(5*x-9,2*x+3)

# Lös ekvationen för x
sol = sp.solve(eqa, x)

# Skriv ut lösningen
print(sol)
