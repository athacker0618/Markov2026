import numpy as np
from time import perf_counter

def newton(f, df, x, tol=1e-12, n=100):
    for _ in range(n):
        x_new = x - f(x)/df(x)
        if x_new <= 0:
            x_new = 1e-12
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

df = lambda x: x*np.exp(-x)

N = 10**6
rng = np.random.default_rng(0)
Results = np.empty(N)

t0 = perf_counter()
for i in range(N):
    u = rng.random()
    f = lambda z: 1 - (z + 1)*np.exp(-z) - u
    x = -np.log1p(-u) + 1e-12
    Results[i] = newton(f, df, x)
t1 = perf_counter()

print(t1 - t0)

