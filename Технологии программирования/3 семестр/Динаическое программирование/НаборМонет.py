n = int(input('Число монет | int >> '))
coins = [int(t) for t in input(f'Достоинства {n}-x монет | array of int >> ').split()]

maxCoins = 0
for i in range(n):
    maxCoins += coins[i]
canGet = [[False for __ in range(n)] for _ in range(maxCoins + 1)]
for _ in range(n):
    canGet[maxCoins][_] = True
print(' i |', '  '.join(list(map(str, coins))), f'| Can get? \n---+{"---" * n}--+--------')
ans = []
for i in [int(maxCoins - t) for t in range(maxCoins + 1)]:
    ansStr = ''
    can = ''
    for j in range(n):
        t = canGet[i].copy()
        if canGet[i][j]:
            t[j] = False
            canGet[i - coins[j]] = t
            ansStr += 'T  '
            can = 'True'
            ans.append(i)
        else: ansStr += 'F  '
    print(str(i).rjust(2), '|', ansStr.rstrip(' '), '|', can)
print('Возможные суммы >> ', ', '.join(list(map(str, sorted(set(ans))))))
            
