def print_mat(mat: list, row: int, col: int):
    for n in range(row):
        for m in range(col):
            print(str(mat[n][m]).ljust(3), end=' ')
        print()

n = int(input("Строки и столбцы n = "))
mt = [[int(s) for s in input("Строка с " + str(n) + " элементов через пробел >>").split()] for i in range(n)]

for i in range(len(mt) // 2):
    for j in range(len(mt[i])):
        if i == j: mt[len(mt) - i - 1][j], mt[i][j] = mt[i][j], mt[len(mt) - i - 1][j]
        if i + j == len(mt) - 1: mt[j][j], mt[i][j] = mt[i][j], mt[j][j]

print_mat(mt, n, n)