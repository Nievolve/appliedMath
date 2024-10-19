import matplotlib as plt
def xygraf(x,y,r, titelx, titley):
    xrange = list(range(0, r))
    yrange = list(range(0, r))


    # Plottning
    plt.figure(figsize=(8, 5))
    plt.plot(xrange, yrange, marker='o', linestyle='-', color='b')
    plt.title(f'{titelx} // {titley}')
    plt.xlabel(titelx)
    plt.ylabel(titley)
    plt.grid(True)

    # Visa grafen
    plt.show()



if __name__ == "__main__":
    xygraf(x=100, y=100,r=100, titelx="XX", titley="YY")