n = int(input("Строки и столбцы (n) = "))
mt = [[int(s) for s in input("Строка с " + str(n) + " элементов через пробел >>").split()] for i in range(n)]

count = []
for i in range(len(mt)):
    sum = 0
    k = 0
    for j in range(len(mt[i])):
        sum = sum + mt[i][j]
    for j in range(len(mt[i])):
        if mt[i][j] > (sum / len(mt[i])):
            k += 1
    count.append(k)

print(count)