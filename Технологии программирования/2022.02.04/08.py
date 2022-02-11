s = input('str > ')
ltt = s.split()
pack, t_pack = [], []
cur_char = ltt[0]

for i in range(len(ltt)):
    if ltt[i] == cur_char:
        t_pack.append(ltt[i])
    else:
        pack.append(t_pack)
        t_pack = []
        cur_char = ltt[i]
        t_pack.append(ltt[i])
pack.append(t_pack)

print(pack)