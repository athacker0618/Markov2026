import numpy as np
import matplotlib.pyplot as plt

N = 10**5
X = np.random.uniform(0, 1, size=(N, 3))
T = np.max(X, axis=1)

plt.figure(figsize=(8, 5))
plt.hist(T, bins=50, density=True, alpha=0.6, label='Simulation')

t = np.linspace(0, 1, 500)
p = 3 * t**2
plt.plot(t, p, 'r-', linewidth=2, label='Theoretical PDF $3t^2$')

plt.xlabel('Time after 6PM (hours)')
plt.ylabel('Density')
plt.title('Distribution of Time When All Friends Have Arrived')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
