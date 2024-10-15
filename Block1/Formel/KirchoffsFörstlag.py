# Definiera strömmarna i noden (positiva för strömmar in i noden, negativa för strömmar ut ur noden)
totalI = 15.0 #Total I i kretsen
delI = []  # Strömmar i ampere
#Skriv in antal delströmmar i forloopen
for k in range(1,3+1):
    invärde = float(input(f"Hur mycket är delström: {k} : "))
    delI.append(invärde)


totalTotalI = totalI-sum(delI)

# Kontrollera
if abs(totalTotalI) < 1e-6:  
    print("Kirchhoffs strömlag uppfylls: summan av strömmarna är 0.")
else:
    print(f"Kirchhoffs strömlag uppfylls inte: summan av strömmarna är {totalTotalI} A.")
