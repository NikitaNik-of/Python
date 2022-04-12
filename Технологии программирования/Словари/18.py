def dels(i):
    ltt = []
    for j in range(i):
        if i % j == 0: ltt.append(j)
    return ltt


nums = [int(n) for n in input('ints /w spaces >> ').split()]
dic = {i:dels(i) for i in nums}
print(dic)