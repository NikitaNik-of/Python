n = int(input("int > "))
st = {i**2 for i in range(1 , n + 1)}
sum = 0
for num in st: sum += num
print(sum)
