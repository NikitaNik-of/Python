import matplotlib.pyplot as plt
import numpy as np
from math import *
from sympy import *

def f_x(x):
    y = (1 + 1/x)**2
    return y


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


t = 1500
a, b = -3, 4
dx = 1e-3
x = np.linspace(a, b, t)
y = f_x(x)

# Подсчет производной
dir1 = (f_x(x + dx/2) - f_x(x - dx/2)) / dx

# Подсчет 2-й производной
dir2 = (f_x(x + 2 * dx) - 2 * f_x(x + dx) + f_x(x)) / np.power(dx, 2)

# Поиск min max по отрезкам
k = 40
ar = [float(a + (abs(b - a) * i / k)) for i in range(k + 1)]
pts = [[], []]
for i in range(len(ar) - 1):
    if not((-0.25 < ar[i] < 0.5) or (-0.25 < ar[i + 1] < 0.5)):
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

# Поиск x, где производная dir = 0
pts1 = [[], [], []]
for x_0 in range(len(dir1)):
    xt = a + (x_0 * abs(b - a) / t)
    if round(dir1[x_0], 2) == 0:
        if len(pts1[0]) == 0:
            pts1[0].append(xt)
            pts1[1].append(f_x(xt))
            pts1[2].append(x_0)
        elif (x_0 - pts1[2][-1] > 2):
            pts1[0].append(xt)
            pts1[1].append(f_x(xt))
            pts1[2].append(x_0)
        else:
            pts1[0][-1] = 0.5 * (pts1[0][-1] + xt)
            pts1[1][-1] = 0.5 * (pts1[1][-1] + f_x(xt))
            pts1[2][-1] = x_0

# Поиск x, где производная dir2 = 0
pts2 = [[], [], []]
for x_0 in range(len(dir2)):
    xt = a + (x_0 * abs(b - a) / t)
    if round(dir2[x_0], 2) == 0:
        if len(pts2[0]) == 0:
            pts2[0].append(xt)
            pts2[1].append(f_x(xt))
            pts2[2].append(x_0)
        elif (x_0 - pts2[2][-1] > 2):
            pts2[0].append(xt)
            pts2[1].append(f_x(xt))
            pts2[2].append(x_0)
        else:
            pts2[0][-1] = 0.5 * (pts2[0][-1] + xt)
            pts2[1][-1] = 0.5 * (pts2[1][-1] + f_x(xt))
            pts2[2][-1] = x_0


all_pts = [pts_[0] + pts1[0] + pts2[0], pts_[1] + pts1[1] + pts2[1]]

# Небольшая сортировка всех точек
for i in range(len(all_pts[0])):
    for j in range(i, len(all_pts[0])):
        if all_pts[0][i] >= all_pts[0][j]:
            all_pts[0][i], all_pts[0][j] = all_pts[0][j], all_pts[0][i]
            all_pts[1][i], all_pts[1][j] = all_pts[1][j], all_pts[1][i]

# Поиск 2-x доп. точек
x_t = all_pts[0][-1] + abs(all_pts[0][-1] - all_pts[0][-2])
all_pts[0].append(x_t)
all_pts[1].append(f_x(x_t))
x_t = all_pts[0][0] - abs(all_pts[0][0] - all_pts[0][1])
all_pts[0].append(x_t)
all_pts[1].append(f_x(x_t))


# Построение эскиза
M = []
for i in range(len(all_pts[0])):
    mi = [np.power(all_pts[0][i], _, dtype=np.float64) for _ in range(len(all_pts[0]))]
    M.append(mi)

X_m = np.linalg.solve(M, np.array(all_pts[1]))
x_m = np.linspace(np.min(all_pts[0]) - 0.15, np.max(all_pts[0]) + 0.15, 100)

# Графики
fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
x_1 = np.linspace(-6, -0.25, 100)
x_2 = np.linspace(0.5, 9, 100)
y_1 = f_x(x_1)
y_2 = f_x(x_2)
ax.plot(x_1, y_1, linewidth=1.5, color='red')
ax.plot(x_2, y_2, linewidth=1.5, color='red')
ax.plot(x_m, g_x(x_m, X_m), linewidth=1, color='black')
ax.scatter(all_pts[0], all_pts[1], linewidth=1.5, color='blue', marker='.')

plt.show()