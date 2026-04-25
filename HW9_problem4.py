import numpy as np
import matplotlib.pyplot as plt

beta = 1.0
m_vals = np.arange(1, 51)

def harmonic(n):
    return sum(1.0/k for k in range(1, n+1)) if n >= 1 else 0.0

E_tau = np.array([harmonic(m-1) / beta for m in m_vals])
tau_det = np.log(m_vals.astype(float)) / beta
tau_det[0] = 0.0  # log(1) = 0

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(m_vals, E_tau,   'o-', color='steelblue', lw=2, ms=4,
        label=r'Stochastic: $H_{m-1}/\beta$')
ax.plot(m_vals, tau_det, 's--', color='crimson',  lw=2, ms=4,
        label=r'Deterministic: $\ln(m)/\beta$')
ax.set_xlabel('Number of particles $m$')
ax.set_ylabel(r'$E[\tau_m]$  $(\beta = 1)$')
ax.set_title(r'Yule process: expected hitting time to $m$ particles')
ax.legend()
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig('HW9_P4.png', dpi=150)
plt.show()
