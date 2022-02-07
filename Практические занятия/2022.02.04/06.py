from math import *

n = int(input('n = '))
binom = [str(int(factorial(n) / factorial(n-k) / factorial(k))) for k in range(n + 1)]
print(' '.join(binom))