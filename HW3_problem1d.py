import numpy as np
import matplotlib.pyplot as plt

ast = np.sqrt(3) - 1

def f(x):
    return (1/3) * x * (1 + x) * np.exp(-x)

def g(x, a=ast):
    return (a**2) * x * np.exp(-a * x)

cst = np.exp(-ast) / (3 * ast**2 * (1 - ast))

x = np.linspace(0, 15, 2000)

plt.figure(figsize=(8, 5))
plt.plot(x, f(x), label='f(x)')
plt.plot(x, cst * g(x, ast), label=r'$c(a^*)\,g_{a^*}(x)$')
plt.xlabel('x')
plt.ylabel('Density')
plt.title(r'$f(x)$ and $c(a^*)g_{a^*}(x)$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
