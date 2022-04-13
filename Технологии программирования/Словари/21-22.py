import json

# Формирование таблицы через input
# n = int(input('c, int >> '))
# m = int(input('v, int >> '))
# c = ['C' + str(_ + 1) for _ in range(n)]
# v = ['V' + str(_ + 1) for _ in range(m)]
# c_data = [ dict( zip(v, list(map(float, input('n*int /w spaces >> ').split())))) for _ in range(n)]
# table = dict(zip(c, c_data))
# print(table)

# Формирование таблицы через file
with open("Технологии программирования\\Словари\\table.txt", 'r2+') as f:
    n = int(f.readline())
    m = int(f.readline())
    c = ['C' + str(_ + 1) for _ in range(n)]
    v = ['V' + str(_ + 1) for _ in range(m)]
    c_data = [ dict( zip(v, list(map(float, f.readline().split())))) for _ in range(n)]
    table = dict(zip(c, c_data))
    print(json.dump(table, sort_keys=True, indent=4))

# Вопрос
q = int(input('V1 > ? | >> '))
vi = 'V1'
for i in range(1, n + 1):
    if table['C' + str(i)][vi] > q: print(table['C' + str(i)])