import sympy as sp
import tkinter as tk
from tkinter import simpledialog

class lawnMower:
    def __init__(self, speed=0.15, cutting_diameter=0.16, turnrate=10, overlap=0.05, holding=0.33):
        self.speed = speed  # Hastighet i meter per sekund
        self.cutting_diameter = cutting_diameter  # Klippdiameter i meter
        self.turnrate = turnrate #Grader per sekund
        self.overlap = overlap #Överlapp i m
        self.holding = holding #m3 volym gräs

class lawnAttribute:
    def __init__(self, shape="kvadrat", sideA=50, sideB=50, overlap=0.1, inputGrass=0.002, turnRadie=180):
        self.shape = shape
        self.sideA = sideA #meter
        self.sideB = sideB #meter
        self.overlap = overlap #meter
        self.input = inputGrass #mängd gräs in i maskinen /s
        self.turnRadie = turnRadie #De svängar som tas på gräsmattan

    def changeSides(self, newSideA, newSideB):
        self.sideA = newSideA
        self.sideB = newSideB
        if newSideA == newSideB:
            self.shape = "kvadrat"
        else:
            pass

# MATH
def vertical(area, speed, cuttingDiameter, turnrate, overlap, shape, turnRadie):
    if shape == "kvadrat":
        lawnRow = sp.sqrt(area) / cuttingDiameter
        grassMeter = lawnRow * sp.sqrt(area)
        speedTime = grassMeter / speed #Sekunder det tar
        turnTime = turnRadie / turnrate * (lawnRow - 1) #Sekunder det tar att göra en sväng

        print(lawnRow)
        print(grassMeter)
        print((speedTime) / 60 / 60)
        print(turnTime)

# TKINTER
def button1_action():
    new_sideA = simpledialog.askfloat("Input", "Ange värde för x (float):")
    new_sideB = simpledialog.askfloat("Input", "Ange värde för y (float):")
    if new_sideA is not None and new_sideB is not None:
        lawn.changeSides(new_sideA, new_sideB)
        message_display.insert(tk.END, f"Gräsmattans nya sidor är: x = {new_sideA}, y = {new_sideB}\n")


def button2_action():
    message_display.insert(tk.END, "Knapp 2 tryckt\n")

def button3_action():
    message_display.insert(tk.END, "Knapp 3 tryckt\n")

# Funktion för att avsluta programmet
def exit_program():
    root.destroy()   

# Givna värden
mower = lawnMower()
lawn = lawnAttribute()
area = lawn.sideA * lawn.sideB

vertical(area, mower.speed, mower.cutting_diameter, mower.turnrate, mower.overlap, lawn.shape, lawn.turnRadie)

# Skapa huvudfönstret
root = tk.Tk()

# Sätt fönstrets titel
root.title("Lawnmower 0.1")

# Skapa en meny
menu = tk.Menu(root)
root.config(menu=menu)

# Add manubutton(dropdown)
menubar = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Meny", menu=menubar)

# Area for menu buttons(dropdown)
menubar.add_command(label="Ändra storlek", command=button1_action)
menubar.add_command(label="Knapp 2", command=button2_action)
menubar.add_command(label="Knapp 3", command=button3_action)

# Message display
message_display = tk.Text(root, height=2, width=50)
message_display.pack(pady=10)

# Area for button on window
exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack(pady=20)  # Placera knappen i fönstret

# Starta en enkel loop för fönstret
root.mainloop()