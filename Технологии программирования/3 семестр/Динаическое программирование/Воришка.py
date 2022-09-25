def house_robber(house_values):
    a = 0  # f(i - 2)
    b = 0  # f(i - 1)
    for val in house_values:
        a, b = b, max(b, a + val)
    return b

n = int(input('Число домов | int >> '))
house_values = [int(t) for t in input(f'Ценность имущества {n}-x домов | array of int >> ').split()]
print('Ответ: ', house_robber(house_values))