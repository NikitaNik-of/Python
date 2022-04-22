import graphlib
import matplotlib.pyplot as plt
import numpy as np
from math import *

# Ввод функции
def f_x(x: float):
    return np.power(np.e, x)


# Подсчет функции
x0 = float(input('x0, float >> '))
x = np.linspace(x0 - 3, x0 + 3)
y1 = f_x(x)

# Подсчет производной
dx = 1e-5
dir = (f_x(x0 + dx/2) - f_x(x0 - dx/2)) / dx
print(dir, f_x(x0))

# Формирование касательной
m = f_x(x0) - (dir * x0)
y2 = dir * x + m

# Построение графика функции с производной
fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(x0, f_x(x0), marker='*')
ax.plot(x, y1, linewidth=1.5, color='black')
ax.plot(x, y2, linewidth=1, color="green")

plt.show()