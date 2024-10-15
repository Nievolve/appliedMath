"""
Trigonometriska funktioner 1/5
Om radförhållandet mellan radiens och grader, matematiskt.

Praktiskt använda för att läsa in:  radier-->grader
                                    grader-->radier
"""
import numpy as np
# För att göra radiens ---> grader
def radToDeg(rad):
    deg = (180/np.pi)*rad
    return deg
# För att göra grader ---> radens
def degToRad(deg):
    rad = (np.pi/180)*deg
    return rad


# Given 
rad = 1     #Fyll in värdet på radiens som ska bli grader#
deg = 1     #Fyll in värdet på grader som ska bli radiens
# Utför
print(f"Radien: {rad} blir till grader: {radToDeg(rad)}")
print(f"Grader: {deg} blir till radiens: {degToRad(deg)}")