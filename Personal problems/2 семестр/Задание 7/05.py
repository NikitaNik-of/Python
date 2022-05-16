import matplotlib.pyplot as plt
import numpy as np
from math import *
# from sympy import *

def f_x(x):
    y = 6 * (np.e ** (x - 1)) - 3 * x - x**3
    return y


# Числовое создание производной
def deriv(x,y):
    x_ = np.zeros((len(x)-1), dtype=np.longdouble)
    y_ = np.zeros((len(x)-1), dtype=np.longdouble)
    for i in range(len(x)-1):
        x_[i] = (x[i+1]+x[i])/2.0
        y_[i] = (y[i+1]-y[i])/(x[i+1]-x[i])
    return x_, y_

# const? const... const!
cols =['#af00fc','#3160ff','#007aff','#0089cc','#008bb9','#008ba7']
dx = 1e-2
x0 = float(input('x0, float >> '))
y0 = f_x(x0)
x = np.linspace(x0 - 2, x0 + 2, 6000)
y = f_x(x)

fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(x, y, linewidth=1.5, color=cols[0], label=f'Исходная функция')
ax.scatter(x0, y0, linewidth=1, color='red', marker='o')

# Поиск ненулевой производной i-порядка
xder, yder = x, y
i, der = 0, 0
while round(der, 1) == 0:
    i += 1
    xder, yder = deriv(xder, yder)
    ax.plot(xder, yder, linewidth=1.5, color=cols[i], label=f'Пр-ная {i}-порядка')
    der = yder[len(yder)//2]
    print(der, i)

# Вывод инфы :p
if (i % 2 == 0) and (der > 0): print('x_0 - Локальный минимум')
elif (i % 2 == 0) and (der < 0): print('x_0 - Локальный максимум')
elif (der < 0): print('x_0 - Точка убывания')
else: print('x_0 - Точка возрастания')

ax.legend()
plt.show()