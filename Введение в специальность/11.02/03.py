from math import *
import numpy as np

def module(a):
    return(sqrt(a[0]**2 + a[1]**2 + a[2]**2))

a1 = np.array([float(s) for s in (input('1) x y z >> ')).split()])
a2 = np.array([float(s) for s in (input('2) x y z >> ')).split()])
a3 = np.array([float(s) for s in (input('3) x y z >> ')).split()])

s = module(np.cross(a2-a1, a2-a3)) * 0.5
print(s, sqrt(2622))

