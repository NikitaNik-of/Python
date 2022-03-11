import numpy as np

np.set_printoptions(precision=3, suppress=True)

n = int(input('Сколько точек? int > '))
M = np.array([[float(num) for num in input('Через пробел координаты (x, y) > ').split()] for _ in range(n)])
mid = np.mean(M, 0)
lens = len(M)
rad = np.array([np.linalg.norm(mid - M[i,:]) for i in range(len(M))]).max()
print(rad, mid)

