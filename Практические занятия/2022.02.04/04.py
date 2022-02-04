n = int(input('n = '))

ltt = []
for i in range(1, n + 1):
    ltt.append([i for i in range(1, i + 1)])
print(ltt)

ltt_ = [[i for i in range(1, j + 1)] for j in range(1, n + 1)]
print(ltt_)