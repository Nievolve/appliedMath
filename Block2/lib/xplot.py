import matplotlib.pyplot as plt

# FUNGERAR!

def xygraf(x):  # Läser in en lista med VALUES, Yrange
    xValue = list(range(len(x)))  
    yrange = [x[k] for k in range(len(x))]  # Y-värden från x

    # Plottning
    plt.figure(figsize=(8, 5))
    plt.plot(xValue, yrange, marker='o', linestyle='-', color='b')
    plt.title(f'X // Y')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)

    # Visa grafen
    plt.show()

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    xygraf(x)
