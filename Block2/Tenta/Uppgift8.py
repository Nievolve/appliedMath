import numpy as np
import sympy as sp

# Funktioner
def calculateSlope(C, t, tau):
    
    return C / tau * np.exp(-t / tau)



#Given information
measure = 15 #min
procent = 72 #%

tauSymbol = sp.Symbol("tauSymbol", real=True,positive=True)
tauEQ = sp.Eq(procent/100,1-sp.exp(-measure/tauSymbol))
tauSolve = sp.solve(tauEQ,tauSymbol)

# A
print(f"Tau = {tauSolve[0]*60:.3g} s")

# Exempelanvändning
C = 5  # Amplitud (slutvärde) i bar
time = np.arange(4,8,1)




resultList = [calculateSlope(C,k,tauSolve[0]) for k in time]

for k in resultList:
    print(k)