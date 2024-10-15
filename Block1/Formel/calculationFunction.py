import numpy as np
import sympy as sp
import matplotlib as plt

def URI():
    print("Vad vill du räkna ut?")
    print("1: U")
    print("2: R")
    print("3: I")
    choice = input(": ")
    if choice == "1":
        R= float(input("Ge värde på R: "))
        I = float(input("Ge värde på I: "))
        U = R*I
        return U
    elif choice == "2":
        U= float(input("Ge värde på U: "))
        I = float(input("Ge värde på I: "))
        R = U/I
        return R
    elif choice == "3":
        U= float(input("Ge värde på U: "))
        R = float(input("Ge värde på R: "))
        I = U/R
        return I
    


