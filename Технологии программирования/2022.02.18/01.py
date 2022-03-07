n = int(input("Строки n = "))
m = int(input("Столбцы m = "))
mt = [[int(s) for s in input("Строка с " + str(m) + " элементов через пробел >>").split()] for i in range(n)]

mtt = [[0] * n for _ in range(m)]

for i in range(n):
    for j in range(m):
        mtt[j][i] = mt[i][j]

for row in mtt:
    print(row)
