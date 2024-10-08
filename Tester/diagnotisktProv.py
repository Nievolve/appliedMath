import sympy as sp
p = sp.symbols("p")
eqa = sp.Eq(3*p+2,(1/2)*p+14)

sol = sp.solve(eqa, p)

print(f"{sol[0]:.2g}")


x = sp.symbols("x")
eqb = sp.Eq(-1/4*x+33/4+1/3*x, 3*x+18)

sol2 = sp.solve(eqb, x)

print(f"{sol2[0]:.3g}")




 #f(x)=ax2+bx+c
x=0
eqc = sp.Eq(x=a*x**2+b*x+c)