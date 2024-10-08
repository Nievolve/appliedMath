import numpy as np
#Läsa in två sidor och grader på motsatt vinkel ger Area till en godtyckig triangel


def area(x,y,angle):
    A = x*y*np.sin(np.radians(angle))/2
    return A


print(f"{area(x=12,y=14,angle=42):.2g}")