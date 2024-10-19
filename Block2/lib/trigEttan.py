import numpy as np
import sympy as sp
import matplotlib as plt

def ettanRule(x):
    rule = np.sin(x)**2+np.cos(x)**2
    if rule == 1:
        return 1
    else:
        return 0



if __name__ == "__main__":
    pass