def chunked(s, n):
    l = [[s[ch] for ch in range(len(s)) if i * n <= ch < (i + 1) * n] for i in range(((len(s) - 1) // n) + 1)]
    return l


st, num = input("str > "), int(input("n = "))
ltt = chunked(st, num)
print(ltt)