n = int(input("n > "))
m = int(input("m > "))
k = int(input("k > "))
x = int(input("x > "))
y = int(input("y > "))
z = int(input("z > "))
t = int(input("t > "))
a = int(input("a > "))

print(f'Только 1 источник: {m + n + k - 2 * (x + y + z) + 3 * t}')
print(f'Только 2 источника: {2 * (m + n + k) - (x + y + z)}')
print(f'Ни одного: {a - (m + n + k - (x + y + z) + t)}')