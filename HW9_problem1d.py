import numpy as np

rng = np.random.default_rng(42)

alpha = 1.0
beta  = 1.0
L     = 20
N     = 10_000

times = np.empty(N)
for trial in range(N):
    i = 0
    t = 0.0
    while i < L:
        rate = alpha if i == 0 else alpha + beta
        t += rng.exponential(1.0 / rate)
        if i == 0:
            i += 1
        else:
            i += 1 if rng.random() < alpha / (alpha + beta) else -1
    times[trial] = t

theory_mean    = L * (L + 1) / (2 * alpha)
empirical_mean = np.mean(times)
empirical_var  = np.var(times, ddof=1)

print(f"Theoretical mean  : {theory_mean:.4f}")
print(f"Empirical mean    : {empirical_mean:.4f}")
print(f"Empirical variance: {empirical_var:.4f}")
