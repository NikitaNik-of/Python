inp = input('int /w spaces >> ')
k = int(input('k >> '))
A = [int(inp.split()[i]) for i in range(k)]
B = []
for i in range(k, len(inp.split())):
    if len(B) == 0:
        while len(A) > 0:
            B.append(A[-1])
            A.pop()
    print(*list(reversed(B)), *A)
    A.append(int(inp.split()[i]))
    B.pop()
print(*list(reversed(B)), *A)