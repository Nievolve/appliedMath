import numpy as np
import UppgiftM23 as up23
#Beräkna grader(acos)


for asin in up23.sinVinklar:
    print(f"Från {asin:.2g} så blir det {np.degrees(np.asin(asin)):.2g} ")

for acos in up23.cosVinklar:
    print(f"Från {acos:.2g} så blir det {np.degrees(np.acos(acos)):.2g} ")

for atan in up23.tanVinklar:
    print(f"Från {atan:.2g} så blir det {np.degrees(np.atan(atan)):.2g} ")