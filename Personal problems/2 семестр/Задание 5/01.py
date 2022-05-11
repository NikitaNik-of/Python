import numpy as np
from math import *
import matplotlib.pyplot as plt

# Ввод функции
def f_x(x):
    return (x - 1)**2 * (x - 3)**2


# Подсчет производной
def f1_x(x0):
    dx = 1e-3
    return (f_x(x0 + dx/2) - f_x(x0 - dx/2)) / dx


x = np.linspace(0, 4, 200)
y = f_x(x)
y1 = f1_x(x)

# Построение графика
fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(x, y, linewidth=1.5, color='red')
ax.plot(x, y1, linewidth=1, color='green')

plt.show()