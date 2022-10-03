from operator import invert


def f(n, x):
    match n:
        case 1:
           return 2*x + 1
        case 2:
           return 3*x*x + 5
        case 3:
           return 0.2*(x**(3)) + 2
            

m = 3
n = int(input('Количество ресурсов для расспределения | int >> ')) + 1
ansTab = [[] for _ in range(m)]
for i in range(n):
    ansTab[0].append(f(1, i))
for i in range(1, m):
    ansTab[i].append(ansTab[i-1][0] + f(i+1, 0))
    for j in range(1, n):
        max = ansTab[i - 1][j] + f(i+1, 0)
        for xj in range(1, j + 1):
            t = ansTab[i - 1][j - xj] + f(i+1, xj)
            if max < t: max = t
        ansTab[i].append(max)

ansX = []
k = n
for i in range(1, m + 1):
    for j in range(k):
        if ansTab[m - i - 1][k - j - 1] + f(m - i+1, j) == ansTab[m-i][k-j-1]:
            k = k - j
            ansX.append(j)
            break
        

print(ansTab, ansX)    
        
