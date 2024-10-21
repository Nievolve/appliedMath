from .lib import libsinuscosius as sc
from .lib import libRadDegConv as rd
cosX1, cosX2= sc.cosX(value=0.6)
sinX1, sinX2= sc.sinX(value=0.6)


print(rd.rad_to_deg(cosX1))

print(rd.rad_to_deg(cosX2))

print(rd.rad_to_deg(sinX1))

print(rd.rad_to_deg(sinX2))
