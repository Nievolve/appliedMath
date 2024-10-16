import sympy as sp

x = sp.symbols("x")
y = sp.symbols("y")

eqxy = sp.Eq(-8, -6*x-10*y)
sol1 = sp.solve(eqxy, x)
for k in sol1:
    print(k)