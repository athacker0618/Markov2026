import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

rng = np.random.default_rng(42)

lam  = lambda t: 0.5 * (1 + (t/30)**2)
T    = 120
lam_max = lam(T)  

arrivals = []
t = rng.exponential(1/lam_max)
while t < T:
    if rng.uniform() < lam(t) / lam_max:
        arrivals.append(t)
    t += rng.exponential(1/lam_max)
arrivals = np.array(arrivals)


E_reports, _ = quad(lam, 0, T)

print(f"Simulated reports : {len(arrivals)}")
print(f"Expected reports  : {E_reports:.1f}")


plt.figure(figsize=(9, 5))
plt.hist(arrivals, bins=120, range=(0, T), color='steelblue', edgecolor='white', linewidth=0.3)
plt.xlabel("Day"); plt.ylabel("Number of reports")
plt.title("Flu reports on campus over 120 days")
plt.xlim(0, T); plt.grid(alpha=0.3)
plt.tight_layout(); plt.savefig("p3c.png", dpi=150); plt.show()
