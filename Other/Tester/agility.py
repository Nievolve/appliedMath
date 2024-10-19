import sympy as sp

def agility(a):
    

    e =(a/6+8)/60
    return e

if __name__ == "__main__":
    for k in range(1,99):
        print(agility(k))