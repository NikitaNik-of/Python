inp = input('int /w spaces >> ')
A = [int(i) for i in inp.split()]
B = []
while inp != '':
    if len(B) == 0:
        while len(A) > 0:
            B.append(A[-1])
            A.pop()
    print(list(reversed(B)), A)
    inp = input('int in stack >> ')
    A.append(int(inp))
    B.pop()