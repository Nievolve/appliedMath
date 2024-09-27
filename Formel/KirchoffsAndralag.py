# Lista med U, U1, U2, U3 osv..
totalU = 12
SubVoltages = [4,3,5,4]  # Exempel på spänningar i kretsen (V)

# Beräkna summan av spänningarna
total_Subvoltage = sum(SubVoltages)
totalTotalVoltage = totalU-total_Subvoltage

# Kontrollera Kirchhoffs andra lag
if totalTotalVoltage == 0:
    print("Kirchhoffs spänningslag uppfylls: summan av spänningarna är 0.")
else:
    print(f"Kirchhoffs spänningslag uppfylls inte: summan av spänningarna är {total_Subvoltage} V. Medan totala spänningen U är :{totalU}")
