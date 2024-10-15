import numpy as np


def Rtemp(T):


    rå = 0.027*10**-6
    A = 2.5*10**-6
    L = 11
    r20= rå*L/A
    a=0.0038
    R= r20*(1+a*(T))
    return R

print(f"82 grader = {Rtemp(T=82):.3g}")
print(f"I mOhm= {Rtemp(T=82)*10**3:.3g}")