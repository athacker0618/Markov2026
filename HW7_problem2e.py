import numpy as np
from scipy.special import i0

rng = np.random.default_rng(42)
lam, T, n_games = 3.0, 48.0, 100_000

N  = rng.poisson(2*lam*T, size=n_games)
NA = rng.binomial(N, 0.5)
D  = 2*(NA - (N - NA))

print(f"{'Quantity':<20} {'Theory':>10} {'Simulated':>10}")
print("-"*42)
print(f"{'E[D(t)]':<20} {0:>10.4f} {np.mean(D):>10.4f}")
print(f"{'Var[D(t)]':<20} {8*lam*T:>10.4f} {np.var(D):>10.4f}")
print(f"{'P(D(t)=0)':<20} {float(np.exp(-2*lam*T)*i0(2*lam*T)):>10.5f} {np.mean(D==0):>10.5f}")
