st = {s.lower() for s in input("str /w spaces > ").split()}
print(*sorted(st)[::-1], sep='\n')