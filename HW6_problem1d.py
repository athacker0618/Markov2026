import numpy as np
import matplotlib.pyplot as plt

P = np.array([
    [0, 1, 0, 0, 0],
    [1/3, 0, 2/3, 0, 0],
    [0, 1/2, 0, 1/2, 0],
    [0, 0, 2/3, 0, 1/3],
    [0, 0, 0, 1, 0]
], dtype=float)

i = np.array([0, 1, 2, 3, 4])

q0 = np.array([0, 0, 1, 0, 0], dtype=float)
q50 = q0 @ np.linalg.matrix_power(P, 50)

pi = np.array([1/12, 1/4, 1/3, 1/4, 1/12], dtype=float)


plt.plot(i, q50, marker='o', label=r'$q_{50}(i)$')
plt.plot(i, pi, marker='s', label=r'$\pi(i)$')
plt.xlabel('i')
plt.ylabel('Probability')
plt.xticks(i)
plt.legend()
plt.grid(True)
plt.show()
