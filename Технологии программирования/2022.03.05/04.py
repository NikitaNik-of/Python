ltt = []
s = input()
while s != '':
    ltt.append(s)
    s = input()
alpha = {l[0].lower() for l in ltt}
print(*sorted(alpha), sep=' ')