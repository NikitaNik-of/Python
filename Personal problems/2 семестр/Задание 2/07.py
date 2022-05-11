import matplotlib.pyplot as plt
import numpy as np
from math import *
from sympy import *

def f_x(x):
    y = (2* x**2 + 3 * x - 2)/(x - 1/2)
    return y

delta = 10
i = 0
dx = 1e-5
x0 = float(input('float, x to ? >> '))
while delta > dx:
    i -= 1
    delta = f_x(x0 + 10 ** i) - f_x(x0 - 10 ** i)
print(delta, i)

x = np.linspace(x0 - 0.5, x0 + 0.5, 100)
y = f_x(x)

fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(x, y, color='black', linewidth=0.5)
ax.scatter(x0, f_x(x0 + 10 ** i), color='blue', marker='.')
plt.show()