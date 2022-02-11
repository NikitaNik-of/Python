from math import *
from numpy import *

print('Формат строки: вводятся координаты вершины.')
trg = [[int(j) for j in input(str(i + 1) +') x, y = ').split()] for i in range(3)]

# lengths = [1-2, 2-3, 3-1]
lths = []
for i in range(3):
    lths.append(sqrt( (((trg[i][0] - trg[(i + 1) % 3][0]) ** 2)) + ((trg[i][1] - trg[(i + 1) % 3][1]) ** 2) ))
print('Длины: ' + str(lths))

# square = int
p = (lths[0] + lths[1] + lths[2]) / 2
s = sqrt(p * (p - lths[0]) * (p - lths[1]) * (p - lths[2]))
print('Площадь: ' + str(s))

#angles = [1, 2, 3]
ang = []
for i in range(3):
    ang.append(degrees(arccos( (lths[(i + 1) % 3]**2 - lths[i]**2 - lths[(i + 2) % 3]**2) / (-2 * lths[i] * lths[(i + 2) % 3]) )))
print('Углы: ' + str(ang))

# r = int
r = s / p
print('Радиус вписанн. окр.: ' + str(r))

# R = int
R = (lths[0] * lths[1] * lths[2]) / (4 * s)
print('Радиус описанн. окр.: ' + str(R))

# med = [1, 2, 3]
med = []
for i in range(3):
    med.append(0.5 * sqrt(2 * (lths[i] ** 2) + 2 * (lths[(i + 2) % 3] ** 2) - (lths[(i + 1) % 3] ** 2)))
print('Сумма медиан: ' + str(med[0] + med[1] + med[2]))
