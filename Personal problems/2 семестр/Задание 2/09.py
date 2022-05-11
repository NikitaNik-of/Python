import matplotlib.pyplot as plt
import numpy as np
from math import *
from sympy import *

def f_x(x):
    y = (x**3 + x**2 - 5*x + 3) / (x**3 - x**2 - x + 1)
    return y


dx = 1e-5
i = 0
delta = 10

x0 = float(input('float, x0 >> '))
x = np.linspace(x0 - 1, x0 + 1, 100)
y = f_x(x)

while delta > dx:
    i -= 1
    delta = f_x(x0 - 10 ** i) - f_x(x0 + 10 ** i)
lim = round(f_x(x0 - 10 ** i), 3)

fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(x, y, color='black', linewidth=0.5)
ax.scatter(x0, lim, color='blue', marker='.')
plt.show()