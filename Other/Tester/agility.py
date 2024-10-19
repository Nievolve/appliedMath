import sympy as sp

import matplotlib.pyplot as plt

# Funktion för att beräkna agility
def agility(a):
    e = ((a/6)+8)/60
    return e

if __name__ == "__main__":
    agility_levels = list(range(1, 99))
    agility_values = [agility(k) for k in agility_levels]

    # Skriv ut agility-nivåer och värden
    for k in agility_levels:
        print(f"Agility level {k}: {agility(k):.3f}")
    

    # Plottning
    plt.figure(figsize=(8, 5))
    plt.plot(agility_levels, agility_values, marker='o', linestyle='-', color='b')
    plt.title('Agility Level vs Agility Value')
    plt.xlabel('Agility Level')
    plt.ylabel('Agility Value')
    plt.grid(True)

    # Visa grafen
    plt.show()
