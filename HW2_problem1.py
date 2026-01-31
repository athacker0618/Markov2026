import numpy as np
import matplotlib.pyplot as plt

g = 4
x0 = 10
N = [100, 1000, 10000]

x = np.linspace(10, 60, 500)
pdf = 3 * x0**3 / x**g

plt.figure(figsize=(12,4))
for i, n in enumerate(N):
    U = np.random.rand(n)
    X = x0 * (1 - U)**(-1/3)

    plt.subplot(1, 3, i+1)
    plt.hist(X, bins=40, density=True, range=(0,60), alpha=0.6)
    plt.plot(x, pdf, 'r', lw=2)
    plt.xlim(0,60)
    plt.title(f'{n} samples')
    plt.xlabel('x')
    plt.ylabel('Density')

plt.tight_layout()
plt.show()
