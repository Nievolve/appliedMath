import sympy as sp

def agility(a):
    

    e =(a/6+8)/60
    return e

if __name__ == "__main__":
    for k in range(1,22):
        print(f"Agility level {k}: {agility(k):.3f}")

    intervall = 0.192-0.136
    print(intervall/20)