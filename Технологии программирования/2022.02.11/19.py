n = int(input("Строки и столбцы n = "))
mt = [[int(s) for s in input("Строка с " + str(n) + " элементов через пробел >>").split()] for i in range(n)]

sim = False
for i in range(len(mt)):
    for j in range(len(mt[i])):
        if (mt[j][i] != mt[i][j]): sim = True
        if sim: exit
    if sim: exit
if sim: print("Симметрии нет")
else: print("Симметрично)") 