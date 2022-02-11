ltt = []
print('Пустая строка = конец ввода')
s = input()
while s != '':
    ltt.append([int(i) for i in s.split()])
    s = input()

maxi = -1
for i in range(len(ltt)):
    if max(ltt[i]) > maxi:
        maxi = max(ltt[i])
mini = ltt[0][0]
for i in range(len(ltt)):
    if min(ltt[i]) < mini:
        mini = min(ltt[i])   
   
print(mini, maxi, maxi + mini)