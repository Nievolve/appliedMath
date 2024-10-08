import sympy as sp
class lawnMower:
    def __init__(self, speed=0.3, cutting_diameter=0.4, turnrate=10):
        self.speed = speed  # Hastighet i meter per sekund
        self.cutting_diameter = cutting_diameter  # Klippdiameter i meter
        self.turnrate = turnrate #Grader per sekund
    
def horizontal(area, speed, cuttingDiamter, turnrate):
    overlap = 0.1
    x=sp.symbols("x")
    lawn = sp.Eq(cuttingDiamter+((cuttingDiamter-overlap)*x, sp.sqrt(area)))
    lawnRow = sp.solve(lawn, x)
    print(lawnRow[0])
sida = 50 #m
Area = sida**2
mower = lawnMower()

horizontal(Area, mower.speed, mower.cutting_diameter,mower.turnrate)