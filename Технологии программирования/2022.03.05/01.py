n = int(input("n > "))
m = int(input("m > "))
k = int(input("k > "))
x = int(input("x > "))
y = int(input("y > "))
z = int(input("z > "))

if (x > n) or (x > m) or (y > m) or (y > k):
    print('Неверные данные')
else:
    print(n + m + k - x - y + z)