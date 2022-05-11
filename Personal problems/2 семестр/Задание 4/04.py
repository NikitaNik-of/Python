import graphlib
import matplotlib.pyplot as plt
import numpy as np
from math import *

# Ввод функции
def f_x(x: float):
    return (x**2)**(1/3)


# Подсчет функции
x0 = 1
dx0 = 0.002
y0 = f_x(x0 - dx0)
dx = 1e-6

# Подсчет производной
dir1 = (f_x(x0 + dx/2) - f_x(x0 - dx/2)) / dx

# Примерное значение в точке x' = 0.998 = x0 - dx0
dy0 = f_x(x0) - dir1 * dx0
print(dy0, y0)
print('dx0 - x0 :', dx0 - dx)


