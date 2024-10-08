import sympy as sp
import tkinter as tk
class lawnMower: # Baserad på 
    def __init__(self, speed=0.15, cutting_diameter=0.16, turnrate=10, overlap=0.05, holding=0.33):
        self.speed = speed  # Hastighet i meter per sekund
        self.cutting_diameter = cutting_diameter  # Klippdiameter i meter
        self.turnrate = turnrate #Grader per sekund
        self.overlap = overlap #Överlapp i m
        self.holding = holding #m3 volym gräs
class lawnAttribute: #Gräsmattans egenskaper och regler
    def __init__(self, shape="kvadrat", sideA=50, sideB=50, overlap=0.1, inputGrass = 0.002, turnRadie=180):
        self.shape = shape
        self.sideA = sideA #meter
        self.sideB = sideB #meter
        self.overlap = overlap #meter
        self.input = inputGrass #mängd gräs in i maskinen /s
        self.turnRadie = turnRadie #De svängar som tas på gräsmattan
    def changeSides(self, newSideA, newSideB):
        self.sideA=newSideA
        self.SideB=newSideB
        if newSideA == newSideB:
            self.shape = "kvadrat"
        else:
            pass
# MATH
def vertical(area, speed, cuttingDiameter, turnrate, overlap, shape, turnRadie):
    if shape == "kvadrat":
        lawnRow = sp.sqrt(area)/cuttingDiameter
        grassMeter = lawnRow *sp.sqrt(area)
        speedTime = grassMeter/speed #Sekunder det tar
        turnTime = turnRadie/turnrate*(lawnRow-1) #Sekunder det tar att göra en sväng

        print(lawnRow)
        print(grassMeter)
        print((speedTime)/60/60)
        print(turnTime)
# TKINTER
def button1_action():
    print("Knapp 1 tryckt")

def button2_action():
    print("Knapp 2 tryckt")

def button3_action():
    print("Knapp 3 tryckt")

# Funktion för att avsluta programmet
def exit_program():
    root.quit()   

        


# Givna värden
mower = lawnMower()
lawn = lawnAttribute()
area = lawn.sideA*lawn.sideB

vertical(area, mower.speed, mower.cutting_diameter,mower.turnrate, mower.overlap, lawn.shape, lawn.turnRadie)




# Skapa huvudfönstret
root = tk.Tk()

# Sätt fönstrets titel
root.title("Lawnmower 0.1")

# Skapa en meny
menu = tk.Menu(root)
root.config(menu=menu)

# Lägga till knappar till menyn
menubar = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Meny", menu=menubar)

# Lägga till 3 menyknappar
menubar.add_command(label="Knapp 1", command=button1_action)
menubar.add_command(label="Knapp 2", command=button2_action)
menubar.add_command(label="Knapp 3", command=button3_action)

# Skapa Exit-knappen
exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack(pady=20)  # Placera knappen i fönstret

# Starta en enkel loop för fönstret
while True:
    try:
        root.update_idletasks()  # Hantera händelser
        root.update()  # Uppdatera gränssnittet
    except tk.TclError:
        break
