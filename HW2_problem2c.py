import numpy as np
from time import perf_counter

N = 10**6
rng = np.random.default_rng(0)

c = 4 / np.e
Results = np.empty(N)
a = 0

t0 = perf_counter()

while a < N:
    y = rng.exponential(scale=2.0)   
    u = rng.random()                
    if u <= (2 * y * np.exp(-y / 2)) / c:
        Results[a] = y
        a += 1

t1 = perf_counter()

print(t1 - t0)
