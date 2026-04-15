import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
lam, T = 3.0, 48.0

def sim_hppp(rate, duration):
    times, t = [], rng.exponential(1/rate)
    while t < duration:
        times.append(t)
        t += rng.exponential(1/rate)
    return np.array(times)

tA = sim_hppp(lam, T)
tB = sim_hppp(lam, T)

plt.figure(figsize=(10, 4))
plt.stem(tA,  np.ones(len(tA)),  linefmt='r-', markerfmt='r|', basefmt='k-', label=f'Team A ({len(tA)} baskets)')
plt.stem(tB, -np.ones(len(tB)),  linefmt='b-', markerfmt='b|', basefmt=' ',  label=f'Team B ({len(tB)} baskets)')
plt.axhline(0, color='k', linewidth=0.8)
plt.xlabel("Time (minutes)"); plt.yticks([])
plt.xlim(0, T); plt.ylim(-1.6, 1.6)
plt.title("Separate interarrivals, $\lambda=3$ min$^{-1}$")
plt.legend(); plt.grid(axis='x', alpha=0.3)
plt.tight_layout(); plt.savefig("p2c.png", dpi=150); plt.show()
