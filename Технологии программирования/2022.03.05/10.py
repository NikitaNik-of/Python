s = input("str /w spaces > ")
ch_set = {ch for ch in s}
ch_list = []
for c in sorted(ch_set):
    count, start = 0, -1
    while True:
        start = s.find(c, start+1)
        if start == -1: break
        count += 1
    # print(f" '{c}' >> {count}")
    ch_list.append((count , c))
ch_list = sorted(ch_list)[::-1]
for inx in range(len(ch_list)) : print(f" '{ch_list[inx][1]}' >> {ch_list[inx][0]}")