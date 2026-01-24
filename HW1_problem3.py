import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(u):
    return u**4 / (1 + u**6)

A, _ = quad(f, 0, 1)
x_vals = np.arange(1, 5.1, 0.1)
N_vals = np.floor(10**x_vals).astype(int)

E_vals = []

for N in N_vals:
    U = np.random.uniform(0, 1, N)
    V = np.random.uniform(0, 1, N)
    E_vals.append(np.mean(V <= f(U)))

plt.figure(figsize=(8, 5))
plt.plot(N_vals, E_vals, marker='o', linestyle='-')
plt.axhline(A, linestyle='--')
plt.xscale('log')
plt.xlabel('N (log scale)')
plt.ylabel('Monte Carlo estimate')
plt.title('Monte Carlo Estimation of Integral')
plt.grid(True)
plt.show()

