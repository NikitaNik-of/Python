import numpy as np
from math import *
import matplotlib.pyplot as plt

# Ввод функции
def f_x(x: float):
    # return x ** 2 + 16 / x - 16
    if x >= 3:
        return (2 * (x**2) * (x - 3)) ** (1/3)
    if x < 3:
        return (2 * (x**2) * (3 - x)) ** (1/3) * -1


def g_x(x: np.linspace, a: list):
    y = 0
    for i in range(len(a)):
        y += float(a[i])*(x**i)
    return y


def fmin(x_l, x_r):
    dx = 1e-2
    for _ in range(1000):
        x_c = 0.5*(x_l + x_r)
        if f_x(x_c - dx) > f_x(x_c + dx):
            x_l = x_c
        else: x_r = x_c
    return x_c


def fmax(x_l, x_r):
    dx = 1e-2
    for _ in range(1000):
        x_c = 0.5*(x_l + x_r)
        if f_x(x_c - dx) < f_x(x_c + dx):
            x_l = x_c
        else: x_r = x_c
    return x_c

dx = 0.001
x = np.linspace(-1.3, 6.3, 200)
y = np.array([f_x(t) for t in x])

# Подсчет производной
dir1 = np.array([(f_x(t + dx/2) - f_x(t - dx/2)) / dx for t in x])

# Поиск min max по отрезкам
ar = [-1, 0.5, 2.5, 4.25, 6]
pts = [[], []]
for i in range(len(ar) - 1):
    mn = fmin(ar[i], ar[i + 1])
    mx = fmax(ar[i], ar[i + 1])
    pts[0].append(mn)
    pts[1].append(f_x(mn))
    pts[0].append(mx)
    pts[1].append(f_x(mx))


# Небольшая сортировка по x
for i in range(len(pts[0])):
    for j in range(i, len(pts[0])):
        if pts[0][i] >= pts[0][j]:
            pts[0][i], pts[0][j] = pts[0][j], pts[0][i]
            pts[1][i], pts[1][j] = pts[1][j], pts[1][i]


# "Чистка" списка точек (if в [x_0...x_n] - монотонная функция, then убираем точки x_1, ... , x_n-1)
pts_ = [[], []]
for i in range(len(pts[0])):
    if (i == 0) or (i == len(pts[0]) - 1):
        pts_[0].append(pts[0][i])
        pts_[1].append(pts[1][i])
    elif not((pts[1][i-1] <= pts[1][i] <= pts[1][i+1]) or (pts[1][i-1] >= pts[1][i] >= pts[1][i+1])):
        pts_[0].append(pts[0][i])
        pts_[1].append(pts[1][i])

# Создание многочлена по точкам
M = []
for i in range(len(pts_[0])):
    mi = [np.power(pts_[0][i], _, dtype=np.float64) for _ in range(len(pts_[0]))]
    M.append(mi)

X_m = np.linalg.solve(M, np.array(pts_[1]))
x_m = np.linspace(np.min(pts_[0]), np.max(pts_[0]), 100)


# Построение графика
fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(x, y, linewidth=1.5, color='red')
ax.plot(x, dir1, linewidth=0.5, color='green')
ax.plot(x_m, g_x(x_m, X_m), linewidth=1, color='black')
ax.scatter(pts[0], pts[1], linewidth=1, color='blue', marker='.')

plt.show()
