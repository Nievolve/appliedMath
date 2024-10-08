import numpy as np
import sympy as sp
import logging 

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("UM210.log", mode='w'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()

def SinBeta(a, b, alfa): 
    sinAlfaValue = np.sin(np.radians(alfa))
    logger.debug("Alfa Value : sinAlfaValue=%s", sinAlfaValue)
    symbolSinBeta = sp.symbols("SinB")
    EqSinBeta = sp.Eq(symbolSinBeta, b * sinAlfaValue / a)
    sol = sp.solve(EqSinBeta, symbolSinBeta)
    returnValue = sol[0]
    logger.debug("Beräkna beta: a=%s, b=%s, alfa=%s", a, b, alfa)
    logger.debug("beta rad: ValueBeta=%s", returnValue)
    return returnValue  # Radianer

def C(b, alfa, gamma):
    alfa_rad = np.radians(alfa)
    gamma_rad = np.radians(gamma)
    c = (b * np.sin(gamma_rad)) / np.sin(alfa_rad)
    logger.debug("Beräkning av c-sidan: alfa=%s, b=%s, gamma=%s", alfa, b, gamma)
    logger.debug("C Sida i funktionen (dm): %s", c)
    return c

def area(a, b, gamma):
    Area = (a * b * np.sin(np.radians(gamma))) / 2
    logger.debug("Beräkning av area: b=%s, c=%s, gamma=%s", b, c, np.radians(gamma))
    logger.debug("Area i funktionen (dm²): %s", Area)
    return Area

# Givet
alfa = 55  # grader
a = 5.0  # dm
b = 6.0  # dm
# Sökt
beta_rad = SinBeta(a, b, alfa)  # Beta i radianer
beta_deg = 180-np.degrees(np.arcsin(float(beta_rad.evalf())))  # Konvertera beta till numeriskt värde och sedan grader
gammaDeg = 180-beta_deg-alfa
c = a * np.sin(np.radians(alfa)) / np.sin(np.radians(gammaDeg))
logger.debug("c sidan : c=%s", c)
logger.debug("Beta (grader): %s", beta_deg)
logger.debug("Gamme i grader: %s", gammaDeg)
Area = area(a,b,gammaDeg) # dm**2
logger.debug("Area = %s", Area)

# Utskrift för att visa resultatet

