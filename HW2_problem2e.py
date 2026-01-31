import numpy as np
import matplotlib.pyplot as plt

N = 10**6
rng = np.random.default_rng(0)
Results = rng.exponential(scale=1.0, size=N) + rng.exponential(scale=1.0, size=N)

xgrid = np.linspace(0, np.percentile(Results, 99.9), 2000)

plt.hist(Results, bins=200, density=True, alpha=0.6)
plt.plot(xgrid, xgrid * np.exp(-xgrid))

plt.xlabel("x")
plt.ylabel("density")
plt.show()
