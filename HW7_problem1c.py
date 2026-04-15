import numpy as np
import matplotlib.pyplot as plt
from scipy.special import i0

lam_A, lam_B = 2/90, 1.5/90
t = np.linspace(0, 90, 500)
rem = 90 - t

P_c = np.where(t < 60,
               np.exp(-(lam_A + lam_B) * rem) * i0(2 * np.sqrt(lam_A * lam_B) * rem),
               lam_B * rem * np.exp(-(lam_A + lam_B) * rem))

plt.figure(figsize=(8, 5))
plt.plot(t[t < 60],  P_c[t < 60],  'b', linewidth=2, label='Score 0–0')
plt.plot(t[t >= 60], P_c[t >= 60], 'r', linewidth=2, label='Score 1–0')
plt.axvline(60, color='k', linestyle='--', label='A scores at $t=60$')
plt.xlabel("Time $t$ (minutes)")
plt.ylabel("$P(\\mathrm{tie} \\mid \\mathrm{history})$")
plt.title("Part (c): A scores at $t = 60$, no other goals")
plt.xlim(0, 90); plt.ylim(0, 1); plt.legend(); plt.grid(alpha=0.3)
plt.tight_layout(); plt.savefig("p1c.png", dpi=150); plt.show()
