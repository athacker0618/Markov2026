import numpy as np

P = np.array([
    [1/2, 1/2, 0,   0,   0, 0],
    [0,   1/2, 1/2, 0,   0, 0],
    [1/3, 0,   1/3, 1/3, 0, 0],
    [0,   0,   0,   1/2, 1/2, 0],
    [0,   0,   0,   0,   0, 1],
    [0,   0,   0,   0,   1, 0]
], dtype=float)

N = 10000
count = 0

for _ in range(N):
    x = 0
    for _ in range(5):
        x = np.random.choice(6, p=P[x])
    if x == 3:
        count += 1
\
  
print(count / N)

