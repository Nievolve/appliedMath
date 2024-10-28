import matplotlib.pyplot as plt

# HOW TO USE!!!
# Läser in en [lista](x)
# y = ska vara len(x)+1
# Funktionen tar in Y(LIST)+L= Längd på x axeln, 
def xyplot(y, L, yLabel):


    # Exempeldata
    x = list(range(1, L))  # X axelns längd


    #Läser in en range 
    plt.plot(x, y, label=yLabel)

    # Sätt etiketter för axlarna
    plt.xlabel(" ")
    plt.ylabel(yLabel)

    # Sätt en titel
    plt.title(yLabel)

    # Ange att varje nivå ska ha en tick
    plt.xticks()  # Detta kommer att visa varje nivå

    # Aktivera rutnät
    plt.grid(True)

    # Visa en legend
    plt.legend()

    # Visa grafen
    plt.show()
