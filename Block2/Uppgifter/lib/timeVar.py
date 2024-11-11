import numpy as np
import matplotlib.pyplot as plt
import logging
import os


## LOGGER

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

##
# Instruktioner:
# KOM IHÅG ATT ALLA ANVÄNDER frekvens(f)
# För [lista] så MATAS endast toppvärde(itopp/utopp) och frekvens(f)in. 
# Tidrange är satt som standard till -20ms-(+)20ms med en stegring på 1 ms. Så med index på 40
# För single värde så MATAS toppvärde(itopp/utopp), frekvens(f) och tid (momentan) in
# U 
# Spänning

def UtAsList(utopp, f, phi):
    T = 1 / f
    w = 2 * f * np.pi
    arange = np.arange(-T, T, 0.001)
    uTime = [utopp * np.sin(w * time) for time in arange]
    title = "Spänning"
    plotter(listToDisplay=uTime, titel1=title)
    return uTime

def UtAsOne(utopp, f, t):
    w = 2 * f * np.pi
    return utopp * np.sin(w * t)

# I
# Strömmen
# Return [LIST]
def ItAsList(itopp, f, phi):
    T = 1 / f
    w = 2 * f * np.pi
    arange = np.arange(-T, T, 0.001)
    itime = [itopp * np.sin(w * time + phi) for time in arange]
    title = "Strömmen"
    plotter(listToDisplay=itime, titel1=title)
    return itime

def IasOne(itopp, f, t, phi):
    w = 2 * f * np.pi
    return itopp * np.sin(w * t + phi)

# Genererar en plotter utifrån en lista

def plotter(listToDisplay, titel1):
    x = np.linspace(0, len(listToDisplay), len(listToDisplay))

    # Skapa plotten
    plt.figure()

    # Rita kurvan
    plt.plot(x, listToDisplay, label=titel1)

    # Lägg till etiketter och titel
    plt.xlabel('Tid (ms)')
    plt.ylabel('Värde')
    plt.title(titel1)
    plt.legend()

    # Visa grafen
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    UtAsList(utopp=325, f=50, phi=np.pi/6)
