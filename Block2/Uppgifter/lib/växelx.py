import numpy as np

def u(utopp,w,t):
    u = utopp*np.sin(w*t)
    return u







if __name__ == "__main__":
    print("Example")
    utopp = 325
    w = 100*np.pi
    t = 10 #ms
    print(f"{u(utopp,w,t*10**-3)}")
    
