n = int(input("Строки n = "))
m = int(input("Столбцы m = "))
mt = [[int(s) for s in input("Строка с " + str(m) + " элементов через пробел >>").split()] for i in range(n)]

#max = [max, i, j]
max = [mt[0][0], 0, 0]
for i in range(len(mt)):
    for j in range(len(mt[i])):
        if max[0] < mt[i][j]:
            max = [mt[i][j], i, j]
print(max[1], max[2])