import numpy as np
from math import *

# Ввод функции
def f_x(x: float):
    return np.log(2 * np.power(x, 3) + 3 * np.power(x, 2))
    # return (6 * x) / (9 * np.power(x, 4) + 1)
    # return np.power(x / 2, -3)


# Подсчет функции
x0 = float(input('x0, float >> '))

# Подсчет производной
dx = 1e-5
dir = (f_x(x0 + dx/2) - f_x(x0 - dx/2)) / dx
print(dir)

# Подсчет 2-й производной
dir2 = (f_x(x0 + 2 * dx) - 2 * f_x(x0 + dx) + f_x(x0)) / np.power(dx, 2)
print(dir2)