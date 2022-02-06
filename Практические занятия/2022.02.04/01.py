ltt = []
print('Пустая строка = конец ввода')
s = input()
while s != '':
    ltt.append([int(i) for i in s.split()])
    s = input()

d = 0
sum = 0
for i in range(len(ltt)):
    d += len(ltt[i])
    for j in range(len(ltt[i])):
        sum += ltt[i][j]

print(sum, d, sum/d)
