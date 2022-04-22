import graphlib
import matplotlib.pyplot as plt
import numpy as np
from math import *

def f_x(x: np.linspace, a: list):
    y = 0
    for i in range(len(a)):
        y += float(a[i])*(x**i)
    return y

pts = [[], []]
n = int(input('n >> '))
for _ in range(n + 1):
    t = input(f'{_} | x, y >> ').split()
    pts[0].append(float(t[0]))
    pts[1].append(float(t[1]))
M = []
for i in range(n + 1):
    mi = [np.power(pts[0][i], _, dtype=np.float64) for _ in range(n + 1)]
    M.append(mi)

X = np.linalg.solve(M, np.array(pts[1]))
x = np.linspace(np.min(pts[0]) - 2, np.max(pts[0]) + 2, 100)

fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(x, f_x(x, X), linewidth=1.5, color='black')
ax.scatter(pts[0], pts[1], linewidth=1, color='red')

plt.show()


