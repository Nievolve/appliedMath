# Funktion för att beräkna tryckdifferensen för ett ventilationssystem med hjälp av SFP-tal

def calculate_pressure_from_sfp(sfp, eta_total, q):
    # Beräkna tryckdifferensen enligt formeln Δp = (SFP * η_tot) / q
    delta_p = (sfp * 1000 * eta_total) / q  # Omvandla SFP från kW till W
    return delta_p

# Parametrar för ventilationssystem
sfp = 0.5  # SFP-tal i kW/(m^3/s) (lägsta värdet för nytt F-system)
eta_total = 0.76  # Fläktens totala verkningsgrad
q = 1.0  # Volymflöde i m^3/s (antaget värde)

# Beräkning av tryckdifferens
delta_p = calculate_pressure_from_sfp(sfp, eta_total, q)

# Utskrift av resultatet för tryckdifferens
print(f"Tryckdifferensen är {delta_p:.2g} Pa")