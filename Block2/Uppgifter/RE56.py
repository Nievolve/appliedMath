# Uppgift:
# 
# Två strömmar, Ĩ₁ = 2.0 ∠ 30° A och Ĩ₂ = 4.0 ∠ 80° A, ska adderas för att beräkna
# den resulterande strömmen, Ĩ = Ĩ₁ + Ĩ₂.
# 
# Lösning:
# 
# Givet:
# 
# - Två växelströmmar i polar form:
#   - Ĩ₁ = 2.0 * e^(j * π/6) A
#   - Ĩ₂ = 4.0 * e^(j * 4π/9) A
# 
# Steg för att lösa uppgiften i Python:
# 1. Omvandla strömmarna från polar form till rektangulär form.
# 2. Addera de komplexa talen.
# 3. Omvandla tillbaka till polar form om så önskas.

from lib import recToPolForm as rc


I_1 = [2.0,30]
I_2 = [4.0,60]

recFormI1 = rc.polToRec(I_1[0], I_1[1])
recFormI2 = rc.polToRec(I_2[0],I_2[1])

addedRecForm1 = complex(recFormI1)+complex(recFormI2)

addedPolarForm1 = rc.recToPol(addedRecForm1)
print(f"I1 som rektangulärform blir = {recFormI1:.2g}")
print(f"I2 som rektanulär form blir = {recFormI2:.2g}")
print(f"")
print(f"Adderad rektanulär form blir = {addedRecForm1:.2g}")
print(f"Adderad polar form blir = {addedPolarForm1[0]:.2g} < {addedPolarForm1[1]:.2g}")