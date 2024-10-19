import numpy as np
import matplotlib.pyplot as plt

def plot_sine_cosine_with_points(period):
    # Skapa ett array med värden från 0 till 2π
    x = np.linspace(0, period, 400)
    
    # Beräkna sinus och cosinus för dessa värden
    sin_values = np.sin(x)
    cos_values = np.cos(x)
    
    # Skapa grafen
    plt.plot(x, sin_values, label='sin(x)')
    plt.plot(x, cos_values, label='cos(x)')
    
    # Lägg till punkter på några specifika värden av x (exempelvis vid varje π/2)
    x_points = np.array([0.6,0])
    sin_points = np.sin(x_points)
    cos_points = np.cos(x_points)
    
    # Använd scatter för att placera punkterna
    plt.scatter(x_points, sin_points, color='red', zorder=5, label='Points on sin(x)')
    plt.scatter(x_points, cos_points, color='blue', zorder=5, label='Points on cos(x)')
    
    # Lägg till etiketter och titel
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sine and Cosine Functions with Points')
    
    # Lägg till en legend
    plt.legend()
    
    # Visa grafen
    plt.show()

if __name__ == '__main__':
    plot_sine_cosine_with_points(period=2*np.pi)
