import numpy as np

P = np.array([
    [9/10, 1/10, 0],
    [0, 7/8, 1/8],
    [2/5, 0, 3/5]])

n = 10000
x = 0
count = 0

for _ in range(n):
    if x == 0:
        count += 1
    x = np.random.choice(3, p=P[x])

frac_G = count/n
print(frac_G)
