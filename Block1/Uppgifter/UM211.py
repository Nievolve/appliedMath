import numpy as np

def cosinusSats(x,y,angle): #Entry cos as degrees
    z=x**2+y**2-2*x*c*np.cos(np.radians(angle))
    
    return z
def beta(a,alfa,c): 
    sinBeta = np.sin(np.radians(alfa))*c/a
    #Omvandala till grader och räkna ut som trubbig
    bD= np.degrees(sinBeta)
    return bD #de
def area(a,b,gamma):
    A= a*b*np.sin(np.radians(gamma))/2
    return A
    
    
#Given information
alfa=35.1 #degrees
b = 21.7 #m
c = 11.2
#3 signifikanta siffror
#Sökt sida
a=np.sqrt(cosinusSats(b,c,alfa))
print(f"{a:.3g}")
beta_deg = beta(a,alfa,c)
betaDegReal= 180-(alfa+beta_deg)
print(betaDegReal)
gamma = 180-betaDegReal-alfa
print(gamma)
Area = area(a,b,gamma)
print(betaDegReal+alfa+gamma)
print (f"{Area:.3g}")


