n = int(input("Строки и столбцы n = "))
mt = [[int(s) for s in input("Строка с " + str(n) + " элементов через пробел >>").split()] for i in range(n)]

sums = [0, 0]
for i in range(n):
    for j in range(n):
        if j < i:
            sums[0] += mt[i][j]
        elif j > i:
            sums[1] += mt[i][j]
print(sums[1] - sums[0])
