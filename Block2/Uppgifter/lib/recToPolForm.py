import cmath as cm
import numpy as np
from lib import libRadDegConv as dc
#Return i index 0 Magnetuden  [0], och i index 1 argumentet (i grader)
# Problem: använder inbyggda funktioner, kan göras om med "rå" matte. Bättre insyn
def recToPol(complex):
    magnetude = abs(complex)
    argument = np.rad2deg(cm.phase(complex))
    #Return magnetude(absolute), argument (degrees)
    return magnetude,argument

# Tar in magnetude och argument i polar form.
# beräknar enligt formel ut realdelen a
#   a = magnetude*cos((Pi/180)*argument))
# beräknar enligt formel ut imaginärdel b
#   b = magnetude*sin((Pi/180)*argument)

def polToRec(magnetude, argument):
    realA = magnetude*np.cos(dc.degToRad(argument))
    imgB = magnetude*np.sin(dc.degToRad(argument))
    ajb=complex(realA,imgB)
    return ajb
if __name__=="__main__":
    pass