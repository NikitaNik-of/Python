st = input("str > ").split()
ltt = [[st[h] for h in range(i, j)] for i in range(len(st)) for j in range(len(st), 0, -1) if i < j]
ltt.append([])
print(sorted(ltt))