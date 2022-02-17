n = int(input("Строки и столбцы (n) = "))
mt = [[int(s) for s in input("Строка с " + str(n) + " элементов через пробел >>").split()] for i in range(n)]
min_mt = [mt[a][a] for a in range(n)]
max_mt = [mt[a][n - (a + 1)] for a in range(n)]
print(min(min_mt) + max(max_mt))