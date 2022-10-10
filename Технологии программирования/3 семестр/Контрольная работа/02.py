var = [0, 3, 8, 22]

n = int(input('n = ? | int >> '))
for i in range(4, n + 1):
    var.append(3*var[i-1] - 2*var[i-3])

print(var[n])