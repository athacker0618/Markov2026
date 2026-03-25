import numpy as np

rng = np.random.default_rng(0)

a = 0.49
n_sims = 10000
max_gen = 200

extinct = 0

for _ in range(n_sims):
    gen = np.array([1], dtype=int)
    died = False

    for _ in range(max_gen):
        children = rng.choice([0, 2], size=gen.size, p=[a, 1 - a])
        total = children.sum()

        if total == 0:
            extinct += 1
            died = True
            break

        gen = np.ones(total, dtype=int)

    if not died:
        pass

print(extinct / n_sims)
