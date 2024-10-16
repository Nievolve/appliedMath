# Bilder nedan visar grafen till sinus- och cosinusfunktion
# för vinklar i intervallet 0 <= x <= 2π rad. Använd graferna för att
# få närmevärde till följande trigonometriska ekvationer i det
# intervallet. Ange även lösningar i vinkelmått grader.

# a) sin(x) = 0.6
# b) sin(x) = -0.9
# c) cos(x) = 0.6
# d) cos(x) = -0.8


import sympy as sp


# Givet (lista)
sinCosList = [0.6,-0.9]

x = sp.symbols("x")
sol = sp.solve_linear(sp.sin(x), 0.6)
print(sol)