import numpy as np

def cosinusSats(x,y,angle): #Entry cos as degrees
    print(np.cos(angle))
    z=x**2+y**2-2*x*c*np.cos(np.radians(angle))
    return z
def Area(b,c,alfa):
    area = b*c*np.cos(np.radians(alfa))/2
    return area
#Given information
alfa=35.1 #degrees
b = 21.7 #m
c = 11.2
#Sökt sida
a=np.sqrt(cosinusSats(b,c,alfa))
print(a)

