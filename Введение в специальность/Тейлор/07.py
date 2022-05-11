import numpy as np
from math import *
import matplotlib.pyplot as plt

# Ввод функции
def f_x(x: float):
    return (3 * x + 1) / (x ** 2 - 3 * x + 2)
    # return 3 / (4 - x ** 2)
    # return np.sin(x)
    # return np.e ** x


dx = 1/4
x0 = float(input('x0, float >> '))
x = np.linspace(x0 - dx, x0 + dx)

# Подсчет производной
dir1 = (f_x(x0 + dx/2) - f_x(x0 - dx/2)) / dx
print(dir1)

# Подсчет 2-й производной
dir2 = (f_x(x0 + 2 * dx) - 2 * f_x(x0 + dx) + f_x(x0)) / np.power(dx, 2)
print(dir2)

# Составление многочлена Тейлора
y = f_x(x)
y1 = f_x(x0) + dir1 * (x - x0)
y2 = f_x(x0) + dir1 * (x - x0) + dir2 * ((x - x0) ** 2) * 0.5

# Построение графика
fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(x, y, linewidth=1.5, color='red')
ax.plot(x, y1, linewidth=1, color='green')
ax.plot(x, y2, linewidth=1, color='blue')

plt.show()