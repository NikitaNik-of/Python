n = int(input('int > '))
lt = [{ch.lower() for ch in input(f"word #{_ + 1} > ")} for _ in range(n)]
st = set()
for i in range(n):
    st = st | lt[i]
print(len(st))