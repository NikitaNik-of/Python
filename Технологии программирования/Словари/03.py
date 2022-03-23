lis1 = list(input('введите ключи ').split())
lis2 = list(input('введите значения ').split())

dict_ = dict(zip(lis1, lis2))

print(*dict_.keys(), 'Ключи')
print(*dict_.values(), 'Значения')