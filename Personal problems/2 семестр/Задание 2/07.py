import matplotlib.pyplot as plt
import numpy as np
from math import *
from sympy import *

# Ввод функций
def f_x(x):
    y = (2* x**2 + 3 * x - 2)/(x - 1/2)
    return y

# Константы для работы программы
delta = 10
i = 0
dx = 1e-5
x0 = float(input('float, x to ? >> '))
y0 = f_x(x0)

# Проверка окрестности у точки x0
while delta > dx:
    i -= 1
    delta = f_x(x0 - 10 ** i) - y0
liml = round(f_x(x0 - 10 ** i), 3)
while delta > dx:
    i -= 1
    delta = f_x(x0 + 10 ** i) - y0
limr = round(f_x(x0 + 10 ** i), 3)
if (limr == liml == y0): print("Непрерывна в точке", x0)
else: print(liml, y0, limr)


# Создание функции
x = np.linspace(x0 - 0.5, x0 + 0.5, 100)
y = f_x(x)

fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(x, y, color='black', linewidth=0.5)
ax.scatter(x0, f_x(x0 + 10 ** i), color='blue', marker='.')
plt.show()