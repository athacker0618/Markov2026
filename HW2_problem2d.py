import numpy as np
from time import perf_counter

N = 10**6
rng = np.random.default_rng(0)

t0 = perf_counter()

Results = rng.exponential(scale=1.0, size=N) + rng.exponential(scale=1.0, size=N)

t1 = perf_counter()

print(t1 - t0)
