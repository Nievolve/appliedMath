import sympy as sp

# Given information
y1 = 1 # sec
y4 = 4 # sec
y1sec = 119
y4sec = 214


# Symby Symbols
C = sp.symbols("C")
tauSymbol = sp.symbols("tauSymbol", positive=True, real=True) # Tillägg för att endast ge positivt realt tal

# Symbo solve function för att ta ut tau (Tidskonstant)
tauEQ = sp.Eq(y1sec/y4sec, (1-sp.exp(-y1/tauSymbol))/(1-sp.exp(-y4/tauSymbol)))
tauSolve = sp.solve(tauEQ,tauSymbol)


# Kontroll funktion #1 (Symby solve function)
spEQ = sp.Eq(119,C*(1-sp.exp(-(1/tauSolve[0]))))
proof1 = sp.solve(spEQ,C)

# Kontroll funktion #2 (Symby solve function)
spEQ = sp.Eq(214,C*(1-sp.exp(-(4/tauSolve[0]))))
proof2 = sp.solve(spEQ,C)




#Presentation
# Skriver ut tidskonstanten
print(f"{tauSolve[0]:.3g}")

if proof1[0] == proof2[0]:
    print(f"C = {proof2[0]:.3g}")
else: 
    print("Något är tjorvens")