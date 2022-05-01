import matplotlib.pyplot as plt
import numpy as np
from math import *
from sympy import *

def f_n(n: int):
    return (sqrt(n + 3) - sqrt((n * n) - 3)) / (((n ** 5) - 4)**(1/3) - ((n ** 4) + 1) ** (1/4))

# Константы для работы алгоритмов
b = True
N_eps = 1
eps = 1e-6
delta = 0
x, y = [], []

# Поиск предела через sympy >> 'pip install -U sympy'
# n = Symbol("x")
# lim_f = float(limit(f_n(n), n, oo))

# Формирование точек
while b:
    N_eps = (N_eps + 1)
    an = f_n(N_eps)
    if len(y) > 1:
        delta = abs(y[-1] - an)
    x.append(N_eps)
    y.append(float(an))
    if (delta > 0) and (delta < eps): b = False
lim_f = round(y[-1], 2)
print(an, delta, N_eps)
print(lim_f)

# Вывод функции
fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.scatter(x, y, color='blue', marker='.', linewidth=0.5)
ax.plot(np.linspace(0, len(x)*1.05), np.linspace(lim_f, lim_f), linewidth=1.5, color='red')

plt.show()
