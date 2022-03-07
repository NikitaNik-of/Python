n = int(input("Строки и столбцы n = "))
mt = [["+" for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            mt[i][j] = "/"
        elif i + j == n - 1:
            mt[i][j] = "/"
        if n % 2 == 1:
            if j == n//2:
                mt[i][j] = "/"
            elif i == n//2:
                mt[i][j] = "/"
for r in mt:
    print(' '.join(r))
