def umn(m1, m2, i, j):
    a = 0
    for r in range(len(m2)):
        a += m1[i][r] * m2[r][j]
    return a


def print_mat(mat: list, row: int, col: int):
    for n in range(row):
        for m in range(col):
            print(str(mat[n][m]).ljust(3), end=' ')
        print()


n = int(input("Строки n = "))
m = int(input("Столбцы m = "))
mt = [[int(s) for s in input("Строка с " + str(m) + " элементов через пробел >>").split()] for i in range(n)]

k = int(input("Столбцы k = "))
mt2 = [[int(s) for s in input("Строка с " + str(k) + " элементов через пробел >>").split()] for i in range(m)]

mt_res = [[umn(mt, mt2, i, j) for j in range(k)] for i in range(n)]
print_mat(mt_res, n, k)
