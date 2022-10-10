fib = [1, 1]

n = int(input('n, n = ? | int >> '))
for i in range(2, n + 1):
    fib.append(fib[i-1] + fib[i-2])

print(fib[n], '|',fib[n] % 10)