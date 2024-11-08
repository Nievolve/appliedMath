import cmath as cm
import numpy as np
import logging
import os

#Return i index 0 Magnetuden  [0], och i index 1 argumentet (i grader)
# Problem: använder inbyggda funktioner, kan göras om med "rå" matte. Bättre insyn
def recToPol(complex):
    magnetude = abs(complex)
    argument = np.rad2deg(cm.phase(complex))
    logger.debug(f"recToPol function, magnetude = {magnetude}")
    logger.debug(f"recToPol function, argument = {argument}")
    #Return magnetude(absolute), argument (degrees)
    return magnetude,argument

# Tar in magnetude och argument i polar form.
# beräknar enligt formel ut realdelen a
#   a = magnetude*cos((Pi/180)*argument))
# beräknar enligt formel ut imaginärdel b
#   b = magnetude*sin((Pi/180)*argument)

def polToRec(magnetude, argument):
    realA = magnetude*np.cos((np.pi / 180) * argument)
    logger.debug(f"polToRec function RealA = {realA}")
    imgB = magnetude*np.sin((np.pi / 180) * argument)
    logger.debug(f"polToRec function imgB = {imgB}")
    ajb=complex(realA,imgB)
    return ajb
    # Skapa mappen 'logging' om den inte redan finns
if not os.path.exists("logging"):
    os.makedirs("logging")

    # Sparar filnamnet som variabel
programName = os.path.splitext(os.path.basename(__file__))[0]

    # Config logging
logFilePath = os.path.join("logging", f"{programName}.log")
logging.basicConfig(
    filename=logFilePath,
    level=logging.DEBUG,  # Set loggningsnivån (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
    
logger = logging.getLogger(programName)




if __name__=="__main__":
    #Tester
    complexTest1 = complex(2,4)
    magnetudeTest1 = 2 # 
    argumentTest1 = 25 # Grader

    print(f"{recToPol(complexTest1)[0]:.2g} < {recToPol(complexTest1)[1]:.2g}")
    print(f"{polToRec(magnetudeTest1,argumentTest1):.2g}")
