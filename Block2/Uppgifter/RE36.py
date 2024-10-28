import numpy as np

#Definera

#Givet

#    Elkomponent: spole (= induktor)
#    Induktansen L = 2,0 mH = 2,0×10−3 H
#    Frekvensen f=50 Hzf=50Hz

#Undersöka

#    Här arbetas med manipulationer med formler (Fall I, enklaste fall).
#    Här tillämpas formel [Fig 3.6], särskild:
#    XL=2πfLXL​=2πfL

#Genomföra
#XL=2πfL≈2×3,14×50×2,0×10−3 Ω≈0,628 ΩXL​=2πfL≈2×3,14×50×2,0×10−3Ω≈0,628Ω

#Utvärdera
#Hantera signifikanta siffror




L = 2.0 *10**-3 #H
f = 50 #Hz

Xl = 2*np.pi*f*L
print(f"{Xl:.2g}")