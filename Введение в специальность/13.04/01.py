from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np
from math import *

def a_n(n: int):
    return np.power(-1, n) / (np.sqrt(n) + 3)

t = int(input())
anv = [a_n(i) for i in range(t)]

x = [i for i in range(1, t)]
y = [sum([anv[j] for j in range(i)]) for i in x]

fig = plt.figure(10)
ax = fig.add_subplot(1, 1, 1)
ax.grid(True)
ax.plot(x, y, linewidth=1.0, marker='+')

plt.show()