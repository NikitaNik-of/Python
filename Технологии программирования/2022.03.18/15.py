n = int(input('int > '))
lt = [len({ch.lower() for ch in input(f"word #{_ + 1} > ")}) for _ in range(n)]
print(*lt, sep=' ')