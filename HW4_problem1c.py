import numpy as np

p = 0.35
q = 0.40
s = 0.25
N = 100000

rng = np.random.default_rng(0)
ending = np.empty(N, dtype=int)

for k in range(N):
    i = 10
    while i > 0:
        r = rng.random()
        if r < s:
            break
        elif r < s + p:
            i += 1
        else:
            i -= 1
    ending[k] = i

print(ending.mean())
