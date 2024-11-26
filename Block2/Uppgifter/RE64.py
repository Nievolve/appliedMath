# Räkneexempel 6.4
# Om en ledare i jämnvikttemperatur med omgivningen, dvs T0 [°C],
# belastas med en konstant ström I [A], ökar ledarens temperatur.
# Den tidsvarierande funktionen T(t), som beskriver hur ledarens
# temperatur varierar med tiden t, lyder enligt:
#
# T(t) = T0 + (Ts - T0) * (1 - exp(-t / τ))
#
# Där:
# Ts = Sluttemperaturen [°C] (ledarens temperatur vid stationärt tillstånd)
# T0 = Initial temperatur [°C] (omgivningens temperatur)
# τ = Tidskonstant (bestämmer hur snabbt systemet når jämvikt)
# t = Tid [s]
#
# Notera: Ts > T0

# τ står för tidskonstant. I detta fall anger τ en mätning av
# ledarens konvektiva förmåga.

# a) Lös analytiskt ekvationen T(t) = a * T0, där a > 1.
#    - Visa lösningen grafiskt.
#    - Gör godtyckliga antaganden.
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
# Antagande 1
caseOne_t_zero = 20
caseOne_t_end = 60
caseOne_tao = 9.0 #min
caseOne_a = 2
caseTwo_time = sp.symbols("caseTwo_time")
# Använder solve funktionen, istället för att manipulera ekvationen
spEQ1 = sp.Eq(caseOne_a*caseOne_t_zero, caseOne_t_zero+(caseOne_t_end-caseOne_t_zero)*(1-sp.exp(-caseTwo_time/caseOne_tao)))

solve = sp.solve(spEQ1)
print(f"{solve[0]:.1f} minuter")

# Antagande 2
caseTwo_t_zero = 20
caseTwo_t_end = 60
caseTwo_tao = 2.0 #min
caseTwo_a = 2
caseTwo_time = sp.symbols("caseTwo_time")
# Använder solve funktionen, istället för att manipulera ekvationen
spEQ2 = sp.Eq(caseTwo_a*caseTwo_t_zero, caseTwo_t_zero+(caseTwo_t_end-caseTwo_t_zero)*(1-sp.exp(-caseTwo_time/caseTwo_tao)))

solve = sp.solve(spEQ2)
print(f"{solve[0]:.1f} minuter")

# PlotterData
timeRange = np.arange(0,10,1/60)


caseOneList = [caseOne_t_zero+(caseOne_t_end-caseOne_t_zero)*(1-sp.exp(-k/caseOne_tao)) for k in timeRange]





plt.plot(timeRange, caseOneList, label="Temperatur")
plt.ylabel("Temperatur (°C)")  
plt.xlabel("Tid (minuter)")  
plt.title("Temperaturutveckling")
plt.legend()
plt.grid()  #
plt.show()


caseTwoList = [caseTwo_t_zero+(caseTwo_t_end-caseTwo_t_zero)*(1-sp.exp(-k/caseTwo_tao)) for k in timeRange]





plt.plot(timeRange, caseTwoList, label="Temperatur")
plt.ylabel("Temperatur (°C)")  
plt.xlabel("Tid (minuter)")  
plt.title("Temperaturutveckling")
plt.legend()
plt.grid()  #
plt.show()