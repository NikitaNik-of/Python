n = int(input("Строки и столбцы (n) = "))
mt = [[int(s) for s in input("Строка с " + str(n) + " элементов через пробел >>").split()] for i in range(n)]

max = mt[0][0]
for i in range(len(mt)):
    for j in range(len(mt[i])):
        if (i >= j) and (max < mt[i][j]):
            max = mt[i][j]
print(max)
