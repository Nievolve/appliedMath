import numpy as np

"""
Räkneexempel 3.8

Beräkna det momentana spänningsuttryck
 u(t)u(t) i kretsen nedan, 
 då huvudströmmen i(t)=48⋅sin⁡(100π⋅t+π6) mA, R=100 ΩR=100 Ω och L=0,15 HL=0,15 H.

a) Utför beräkningen grafiskt i tidsrepresentation, dvs med tidsvariabla strömmen och spänningen.

b) Utför beräkningen analytiskt i visarrepresentation, dvs med strömsummare och spänningsvisare.

Givet

    Elkrets med tre komponenter i seriekoppling
        Spänningskälla: Växelström U(t)=?U(t)=?
        Resistor: Resistansen R=100 ΩR=100 Ω
        Ideal spole: Induktansen L=0,15 HL=0,15 H

    Huvudströmmen: i(t)=48⋅sin⁡(100π⋅t+π6)i(t)=48⋅sin(100π⋅t+6π​) mA
        I^=48 mA , ω=100π rad/s, β=π/6 rad(faskonstanten)

Sökt

    Den momentana spänningen u(t)u(t), dvs den tidsvariabla funktionen som beskriver funktionsregeln U(t)U(t).
        a) Metoden: Tidsrepresentation (grafiskt)
        b) Metoden: Visarrepresentation

        Undersöka

    Här tillämpas Kirchhoffs spänningslag.
    För metoden a) kombineras teoretiska uppförande med grafritning av grafavläsning.
    För metoden b) tillämpas geometri och trigonometri.
"""

import numpy as np
from lib import plotter
def Ur(R,Itopp,w,t,V):
	return R*Itopp*np.sin(w*t+V)
def Ul(Xl,Itopp,w,t,V,fasförskjutning):
	return Xl*Itopp*np.sin(w*t+(V+fasförskjutning))
def Xl(L,w):
	return L*w


#Givet
Itopp = 48*10**-3 #A
L = 0.15
R = 100

f = 50
w = 2*np.pi*f
V = np.pi/6
fasförskjutning= np.pi/2
intervalT = np.arange(0.000,0.02,0.001)
ut= [Ur(R,Itopp,w,k,V)+Ul(Xl(L,w),Itopp,w,k,V,fasförskjutning)for k in intervalT]
Ylabel = "U(t)"
plotter.listPlotter(ut)
	
print(max(ut))