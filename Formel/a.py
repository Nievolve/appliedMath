
def kabelm():
    try:
        # Fråga efter resistans och area och omvandla till flyttal
        print("Ta reda på längden på kabeln baserat på uppmätt resistans och area.")
        r = float(input("Ange den uppmätta resistansen (ohm): "))
        a = float(input("Ange den uppmätta arean (mm²): "))
        
        # Kontrollera att värdena är positiva
        if r <= 0 or a <= 0:
            print("Resistansen och arean måste vara positiva tal!")
            return

        # Resistivitet för koppar
        p = 0.0175  # ohm * mm² / m

        # Beräkna längden
        l = (r * a) / p

        # Visa resultatet med en tydlig enhet
        print(f"Kabellängden är {l:.2f} meter.")

    except ValueError:
        print("Fel: Ange giltiga numeriska värden för resistans och area.")
def area():
    print("Ta reda på area")
    p = 0.0175  # ohm * mm² / m
    l = float(input("Kabelsn längden: "))
    r = float(input("Resitens: "))
    a = p*l/r
    print(f"Arean är {l:.2f} mm2.")
# Anropa funktionen

def meny():
    while True:
        print("\n--- Kabelmeny ---")
        print("1. Beräkna kabellängd")
        print("2. Beräkna kabelarea")
        print("3. Avsluta")
        val = input("Välj ett alternativ (1-3): ")

        if val == '1':
            kabelm()
        elif val == '2':
            area()
        elif val == '3':
            print("Avslutar programmet.")
            break
        else:
            print("Felaktigt val, försök igen.")

# Starta menyn
meny()
