# a_n = (2n + 1)/(3n - 5), a = 2/3

import matplotlib.pyplot as plt
import numpy as np
from math import *

# Константы для работы алгоритмов
width = 100
b = True
N_eps = 1
M = 100000000
eps = 1e-7
am = 2/3
x, y = [], []

# Поиск предела (an)
while b:
    N_eps += 1
    an = (2 * N_eps + 1) / (3 * N_eps - 5)
    delta = abs(am - an)
    if len(x) < width:
        x.append(N_eps)
        y.append(an)
    if delta < eps: b = False
print(an, delta, N_eps)

# Вывод функции
fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.scatter(x, y, color='blue', marker='.', linewidth=0.5)
ax.plot(np.linspace(0, width + 1), np.linspace(2/3, 2/3), linewidth=1.5, color='red')

plt.show()
