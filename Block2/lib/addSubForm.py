import numpy as np
# Läser in alfa och beta vinkel och ger tillbaka dem i regel
def rule(alfa, beta):
    sinAlfaBeta = np.sin(np.sin(alfa)*np.cos(beta)+np.cos(alfa)*np.sin(beta))
    cosAlfaBeta = np.sin(np.sin(alfa)*np.cos(beta)-np.cos(alfa)*np.sin(beta))

    return (sinAlfaBeta, cosAlfaBeta)



if __name__ == "__main__":
    rule(alfa=30,beta=45)
