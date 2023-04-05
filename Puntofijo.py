import numpy as np
import matplotlib.pyplot as plt

def funcion1(x):
    return (x+1)**(1/3)

def punto_fijo(g, x0, tol=0.001, nmax=100):
    x = g(x0)
    error = abs(x - x0)
    niter = 1

    print("n\t G(n-1)\t\t error")

    while error > tol and niter < nmax:
        print(f"{niter}\t {x:.10f}\t {error:.10f}")

        x0 = x
        x = g(x0)
        error = abs(x - x0)
        niter += 1

    print(f"{niter}\t {x:.10f}\t {error:.10f}")

    return x, error, niter


g = lambda x: (x+1)**(1/3)
x0 = 1

x, error, niter = punto_fijo(g, x0)

print(f"\nLa raíz de la función es x = {x:.6f} (error = {error:.6f}, iteraciones = {niter})")
