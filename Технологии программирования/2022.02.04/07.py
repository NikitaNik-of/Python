from math import *

def pascal(n):
    for i in range(n + 1):
        binom = [str(int(factorial(i) / factorial(i-k) / factorial(k))) for k in range(i + 1)]
        print(' '.join(binom))


n = int(input('n = '))
pascal(n)