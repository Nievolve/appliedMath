import numpy as np

def Xl(w,L):
    Xl=w*L
    return Xl
def w(f):
    w=2*np.pi*f
    return w
def L(Xl,w):
    L = Xl/w
    return L

print(f"A) om L är 50 microFarad och frekvensen är 900Hz så blir Xl: {Xl(w(f=900),L=50*10**-6):.2g} Ohm")
print(f"B) Om spolen har en reaktans på 120k Ohm och en frekvens på 1.2 MHz så blir L: {L(Xl=12*10**4, w=w(f=1.2*10**6)):.2g} Henry")