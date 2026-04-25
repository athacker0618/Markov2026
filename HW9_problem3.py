import numpy as np
from math import lgamma, log, exp

def erlang_b(s, rho):
    log_num = s * log(rho) - lgamma(s + 1)
    terms   = [k * log(rho) - lgamma(k + 1) for k in range(s + 1)]
    max_t   = max(terms)
    log_den = max_t + log(sum(exp(t - max_t) for t in terms))
    return exp(log_num - log_den)

rho = (1/15) / (1/10)

for s in range(1, 8):
    print(f"s = {s},  B = {erlang_b(s, rho):.4f}")
