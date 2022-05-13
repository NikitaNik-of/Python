inp = input('int /w spaces >> ')
stack = []
for j in inp.split():
    i = int(j)
    if len(stack) == 0: stack.append((i, i))
    elif i > stack[-1][1]: stack.append((i, i))
    else: stack.append((i, stack[-1][1]))
print(stack)
print(stack[-1][1])