import matplotlib.pyplot as plt
import numpy as np

# Genererar en plotter utifrån en lista

def listPlotter(listToDisplay):
    x = np.linspace(0, round(len(listToDisplay)), len(listToDisplay))

    # Skapa plotten
    plt.figure()

    # Rita kurvan
    plt.plot(x, listToDisplay, label="Imported")

    # Lägg till etiketter och titel
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Graf")
    plt.legend()

    # Visa grafen
    plt.grid(True)
    plt.show()


# Läser in värden från exempelvis komponenter i en krets. Kan användas för att ta reda (snabbt) om en krets/last är induktiv eller kapacitit.

def visarPlotter(base, load):
    # Skapa linjen längs x-axeln, från origon[0] till värdet
    x1 = [0, base]  # Från 0 till xLength
    y1 = [0, 0]        # Y är konstant 0

    # Skapa linjen längs y-axeln
    x2 = [base, base]  # X är konstant vid xLength
    y2 = [0, load]        # Från 0 till yLength
    # Diagonal linje för att visa U
    x_diag = [0, base]
    y_diag = [0, load]



    # Plotta båda linjerna
    plt.figure()
    plt.plot(x1, y1, label="Resistant load", color="blue")
    plt.plot(x2, y2, label="Induktiv/Kapacitiv load", color="red")
    plt.plot(x_diag, y_diag, linestyle='--', color="green", label="U")

        
    # Skriv ut värdena bredvid base och load linjerna
    plt.text(base, 0, f"Base: {base}", fontsize=12, color="blue", ha="left")
    plt.text(base, load, f"Load: {load}", fontsize=12, color="red", ha="left")
    plt.text(0, 0, f"{np.sqrt(base**2+abs(load**2)):.2f}", fontsize=12, color="black", ha="right")




    # Lägg till etiketter och titel
    plt.xlabel('Ur')
    plt.ylabel('Ul/Uc')
    plt.title("Visar diagram")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Markera x-axeln
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Markera y-axeln
    plt.legend()
    plt.grid(True)

    # Visa grafen
    plt.show()




if __name__ == "__main__":

    visarPlotter(base=5.2,load=-3.7)