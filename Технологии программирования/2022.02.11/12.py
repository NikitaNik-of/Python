n = int(input("Строки и столбцы (n) = "))
mt = [[int(s) for s in input("Строка с " + str(n) + " элементов через пробел >>").split()] for i in range(n)]
s = 0
for a in range(n):
    s = mt[a][a] + s
print(s)