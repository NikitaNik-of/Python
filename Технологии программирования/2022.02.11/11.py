def print_mat(mat: list, row: int, col: int):
    mat.reverse()
    for n in range(row):
        mat[n].reverse()
        for m in range(col):
            print(str(mat[n][m]).ljust(3), end=' ')
        print()

n = int(input("Строки n = "))
m = int(input("Столбцы m = "))
mt = [[int(s) for s in input("Строка с " + str(m) + " элементов через пробел >>").split()] for i in range(n)]
print_mat(mt, n, m)