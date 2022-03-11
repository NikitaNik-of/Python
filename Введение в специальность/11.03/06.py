import numpy as np
from math import *

np.set_printoptions(precision=3, suppress=True)

n = int(input('Сколько точек? int > '))
M = np.array([[float(num) for num in input('Через пробел координаты (x, y) > ').split()] for _ in range(n)])
fi = int(input('Угол поворота? int > '))
T = np.array([[cos(radians(fi)), sin(radians(fi))], [0 - sin(radians(fi)), cos(radians(fi))]])
M1 = np.dot(M, T)
print (M, M1, sep='\n\n')
print(np.mean(M1, 0))

