import numpy as np
import matplotlib.pyplot as plt

def y1_theory(t):
    return 1/4 - (1/12)*np.exp(-2*t) + (1/6)*np.exp(-t)*(np.cos(t) - 2*np.sin(t))

rng = np.random.default_rng(42)
t_eval = np.linspace(0, 5, 400)
N_values = [100, 1_000, 10_000, 100_000]

fig, axes = plt.subplots(2, 2, figsize=(11, 8), constrained_layout=True)

for ax, N in zip(axes.flatten(), N_values):
    s0 = rng.choice([1, 2], size=N, p=[1/3, 2/3])
    f_t = np.zeros(len(t_eval))
    for j, t in enumerate(t_eval):
        n_trans = rng.poisson(t, size=N)
        states  = ((s0 - 1 + n_trans) % 4) + 1
        f_t[j]  = np.mean(states == 1)

    ax.plot(t_eval, f_t, color='steelblue', lw=1.3, label='Simulation $f(t)$')
    ax.plot(t_eval, y1_theory(t_eval), color='crimson', lw=2, label='Theory $y_1(t)$')
    ax.axhline(0.25, color='gray', lw=0.8, ls='--', label=r'$\pi_1=1/4$')
    ax.set_xlim(0, 5); ax.set_ylim(0, 0.5)
    ax.set_xlabel('Time $t$'); ax.set_ylabel('Fraction in state 1')
    ax.set_title(f'$N = {N:,}$', fontweight='bold')
    ax.legend(); ax.grid(alpha=0.25)

fig.suptitle('Problem 1(e): Fraction of chains in state 1 vs. time')
plt.savefig('problem1_simulation.png', dpi=160, bbox_inches='tight')
plt.show()
