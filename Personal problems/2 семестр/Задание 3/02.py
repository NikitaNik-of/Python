import graphlib
import matplotlib.pyplot as plt
import numpy as np
from math import *

# Ввод функции
def f_x(x: float):
    return (x**3 + 2) / (x**3 - 2)


# Подсчет функции
x0 = 2
x = np.linspace(x0 - 3, x0 + 3, 200)
# Чтобы красиво было (.❛ ᴗ ❛.)
xl = np.linspace(1.31, x0 + 3, 100)
xr = np.linspace(x0 - 3, 1.2, 100)
yl = f_x(xl)
yr = f_x(xr)

# Подсчет производной
dx = 1e-5
dir = (f_x(x0 + dx/2) - f_x(x0 - dx/2)) / dx
print(dir, f_x(x0))

# Формирование касательной
m = f_x(x0) - (dir * x0)
y2 = dir * x + m

# Формирование нормали
k = -1 / dir
m = f_x(x0) - (k * x0)
y3 = k * x + m

# Построение графика функции с производной
fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(x0, f_x(x0), marker='*')
ax.plot(xl, yl, linewidth=1.5, color='black')
ax.plot(xr, yr, linewidth=1.5, color='black')
ax.plot(x, y2, linewidth=1, color="green")
ax.plot(x, y3, linewidth=1, color="red")

plt.show()