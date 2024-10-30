# Beräkna det momentana spänningsuttryck u(t) i kretsen.
# Moment 4 Trigonometriska funktioner sidan 4/11 Del 5/5

# Beräkna det momentana spänningsuttryck u(t) i kretsen nedan, då
# huvudströmmen i(t) = 48 ⋅ sin(100π ⋅ t + π/9) mA, R = 100 Ω och C = 55 μF.

    # a) Utför beräkningen grafiskt i tidsrepresentation, dvs med tidsvariabla strömmen och spänningen.
    # b) Utför beräkningen analytiskt i visarrepresentation, dvs med strömvisare och spänningsvisare.

# Lösning
    # Definera
        # Givet:
        # - Elkrets med tre komponenter i seriekoppling
            # - Spänningskälla: Växelström U(t) = ?
            # - Resistor: Resistansen R = 100 Ω
            # - Ideal kondensator: Kapacitansen C = 55 μF = 55 ⋅ 10⁻⁶ F

        # Huvudströmmen: i(t) = 48 ⋅ sin(100π ⋅ t + π/9) mA

        # => Î = 48 mA = 48 ⋅ 10⁻³ A, ω = 100π rad/s, β = π/9 rad (faskonstanten)

        # Obs! π/9 ≈ 20°

# Sök:
    # - Den momentana spänningen u(t), dvs den tidsvariabla funktionen som beskriver funktionsregeln u(t).
    # a) Metoden: Tidsrepresentation (grafiskt)
    # b) Metoden: Visarrepresentation

# Undersöka:
    # - Här tillämpas Kirchhoffs spänningslag.
    # - För metoden a) kombineras teoretiska uppförande med grafritning av grafavläsning
    # - För metoden b) tillämpas geometri och trigonometri

import numpy as np
from lib import xyPlot as XY

def Ur(R,Itopp,w,t,V):
    return R*Itopp*np.sin(w*t+V)
def Uc(xc,Itopp,w,t,V,faskompensering):
    return xc*Itopp*np.sin(w*t-V+faskompensering)
def Xc(w,C):
    return 1/(w*C)
# Givet
V = np.pi/9
Itopp = 48*10**-3 #A
R = 100 # Ohm
C = 55*10**-6 #microFarad
f = 50
w = 2*np.pi*f
faskompensering=-np.pi/2 #negativ 90 grader för det är en kapacitivbelastning

print(f"{Xc(w,C):.4g}")


intervalT = np.arange(0.00,0.02,0.001)

ut = [Ur(R,Itopp,w,k,V)+Uc(Xc(w,C),Itopp,w,k,V,faskompensering)for k in intervalT]
ur = [Ur(R,Itopp,w,k,V)for k in intervalT]
uc = [Uc(Xc(w,C),Itopp,w,k,V,faskompensering)for k in intervalT]
Ylabel="Varför tar jag inte bort denna"
XY.xyplot(ut,len(ut)+1,Ylabel)
XY.xyplot(ur,len(ur)+1,Ylabel)
XY.xyplot(uc,len(uc)+1,Ylabel)