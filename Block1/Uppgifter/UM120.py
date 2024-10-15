def fVent(Pif,qV):
    fVent = Pif/qV
    return fVent

# Exempelanvändning:
Pif= 0.6

qV = 350*10**-3Y #meter3/sek

sfp_result = fVent(Pif,qV)
print(f"Fvent : {fVent(Pif,qV):.3g}")
