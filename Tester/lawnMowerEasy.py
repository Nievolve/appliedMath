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
    def __init__(self, shape="", sideA=50, sideB=50, overlap=0.1, inputGrass = 0.002):
        self.shape = shape
        self.sideA = sideA #meter
        self.sideB = sideB #meter
        self.overlap = overlap #meter
        self.input = inputGrass #mängd gräs in i maskinen /s
    def changeSides(self, newSideA, newSideB):
        self.sideA=newSideA
        self.SideB=newSideB
        if newSideA == newSideB:
            self.shape = "kvadrat"
        else:
            pass

def vertical(area, speed, cuttingDiameter, turnrate, overlap, shape):
    if shape == "kvadrat":
        lawnRow = sp.sqrt(area)/cuttingDiameter

        print(lawnRow)
    

        
    

# Givna värden

mower = lawnMower()
lawn = lawnAttribute()
area = lawn.sideA*lawn.sideB

vertical(area, mower.speed, mower.cutting_diameter,mower.turnrate, mower.overlap)