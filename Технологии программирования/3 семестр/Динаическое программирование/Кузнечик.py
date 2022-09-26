# Забыл какое условие было в презентации, поэтому использовал это 👉 https://algorithmica.org/tg/cache-basics

N = int(input('Число ступенек для кузнечика | int >> '))
cache = [0] * (N + 1)
cache[1] = 1
cache[2] = 1
cache[3] = 2
for i in range(4, N + 1):
    cache[i] = cache[i - 3] + cache[i - 2] + cache[i - 1]
print(cache(N))