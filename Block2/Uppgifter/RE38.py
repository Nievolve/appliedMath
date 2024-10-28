import numpy as np

"""
Genom en spole med induktansen 0,8 H går en ström.
Beräkna den inducerade spänningen över spolen då strömmen:
a) är konstant 10 A
b) ökar linjärt från 0 till 0,5 A på 10 ms.
c) är en sinusformad ström i(t) = 0,75 * sin(100πt) [A].

Definera

Givet

    Elkomponent: spole
    Induktansen L = 0,8 H
    a) Likström I = 10 A
    b) Linjär funktion 0-0.5 A på 10ms
    c) Sinusfunktion i(t)=iTOP*sin(w*t)

Sökt

    a), b) och c)
    Den inducerade spänningen över spolen

Undersöka
    Här övar vi med formeln [F.3.3.5]
        U (t)=L* di(t)/dt
    Förkunskaper: linjära funktioner, i synnerhet k-formel (= differenskvot).
    Matematik 2a.
"""

def constI(t):
    L = 0.8 #H
    pass

