import matplotlib.pyplot as plt
import numpy as np
from math import *
from sympy import *


def geoSum(a1, q, n):
    return a1 * (1 - q**n)/(1 - q)


def f_n(n: int):
    return geoSum(1, 1/3, n) / geoSum(1, 1/5, n)

# Константы для работы алгоритмов
b = True
N_eps = 1
eps = 1e-15
delta = 0
x, y = [], []
s_y = []

# Поиск предела через sympy >> 'pip install -U sympy'
n = Symbol("x")
lim = float(limit(f_n(n), n, oo))

# Формирование точек
while b:
    N_eps = (N_eps + 1)
    an = f_n(N_eps)
    if len(y) > 0:
        delta = abs(y[-1] - an)
        s_y.append(s_y[-1] + an)
    else:
        s_y.append(an)
    x.append(N_eps)
    y.append(float(an))
    if (delta > 0) and (delta < eps): b = False
lim_f = round(y[-1], 6)
print(an, delta, N_eps)
print(lim_f, lim)

# Вывод функции
fig = plt.figure(10)
ax = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
ax.grid(True)
ax2.grid(True)
ax.scatter(x, y, color='blue', marker='.', linewidth=0.5)
ax2.scatter(x, s_y, color='green', marker='.', linewidth=0.5)
ax.plot(np.linspace(0, len(x)*1.05), np.linspace(lim_f, lim_f), linewidth=1.5, color='red')

plt.show()
