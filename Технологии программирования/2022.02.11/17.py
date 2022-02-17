n = int(input("Строки и столбцы (n) = "))
mt = [[int(s) for s in input("Строка с " + str(n) + " элементов через пробел >>").split()] for i in range(n)]

# Правая, верхняя, левая, нижняя
sum = [0, 0, 0, 0]
for i in range(len(mt)):
    for j in range(len(mt[i])):
        if j < i:
            if j + i < len(mt) - 1:
                sum[2] += mt[i][j]
            elif j + i > len(mt) - 1:
                sum[3] += mt[i][j]
        elif j > i:
            if j + i < len(mt) - 1:
                sum[1] += mt[i][j]
            elif j + i > len(mt) - 1:
                sum[0] += mt[i][j]
            
print(sum)
