import numpy as np

# Läser in alfa och beta vinklar (i grader) och ger tillbaka deras kombinerade sin- och cos-värden
def rule(alfa, beta):
    # Konvertera grader till radianer
    alfa_rad = np.deg2rad(alfa)
    beta_rad = np.deg2rad(beta)
    
    # Beräkna sin och cos för (alfa + beta)
    sinAlfaBeta = np.sin(alfa_rad + beta_rad)
    cosAlfaBeta = np.cos(alfa_rad + beta_rad)

    return sinAlfaBeta, cosAlfaBeta

if __name__ == "__main__":
    sin_value, cos_value = rule(alfa=30, beta=45)
    print(f"sin(30° + 45°) = {sin_value}")
    print(f"cos(30° + 45°) = {cos_value}")

