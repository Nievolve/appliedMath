import numpy as np


def Rtemp(T):
    rå = 0.027*10**-6
    l = 11
    A = 2.5 #mm2

    Rl = rå*l/A
    print(f"Rl = {Rl:2g}")
    a = 0.0038 #Grader vid C-1
    Temp= Rl*(1+a*(T))
    print(f"TempR= {Temp*10**9}")

Rtemp(T=82)