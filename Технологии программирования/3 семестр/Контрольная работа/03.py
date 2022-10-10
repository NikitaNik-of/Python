ansGrid = [[] for _ in range(8)]
ansGrid[0].extend([1, 1, 1, 1, 1, 1, 1, 1])

for i in range(1, 8):
    for j in range(8):
        if j==0: ansGrid[i].append(ansGrid[i-1][1])
        elif j==7: ansGrid[i].append(ansGrid[i-1][6])
        else: ansGrid[i].append(ansGrid[i-1][j-1] + ansGrid[i-1][j+1])
# print(ansGrid)

cord = list(map(int, input('Введите координаты клетки, если 0,0 - это верхняя левая клетка | x y (each value < 8) >> ').split()))
print('Варианты:', ansGrid[cord[0]][cord[1]])
