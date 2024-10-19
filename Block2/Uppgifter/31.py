# Bilder nedan visar grafen till sinus- och cosinusfunktion
# för vinklar i intervallet 0 <= x <= 2π rad. Använd graferna för att
# få närmevärde till följande trigonometriska ekvationer i det
# intervallet. Ange även lösningar i vinkelmått grader.

# a) sin(x) = 0.6
# b) sin(x) = -0.9
# c) cos(x) = 0.6
# d) cos(x) = -0.8
from ..lib import sinCosGraf as graf
import numpy as np
graf.plot_sine_cosine(period=np.pi, pointA=0.6, pointB=1)
