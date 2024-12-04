import sympy as sp
# Funkar EJ


def kondensator_laddning(t):
    q = 11.7 * sp.exp(-(0.0659 * t)) + 11.7
    return q

t = 7.17
q_t = kondensator_laddning(t).evalf()

print(f"{q_t:.3g}")
