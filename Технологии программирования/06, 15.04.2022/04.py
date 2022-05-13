import json
with open("Технологии программирования\\СР6, 15.04.2022\\table.txt", 'r+') as f:
    n = int(f.readline())
    m = int(f.readline())
    c = ['C' + str(_ + 1) for _ in range(n)]
    v = ['V' + str(_ + 1) for _ in range(m)]
    c_data = [ dict( zip(v, list(map(float, f.readline().split())))) for _ in range(n)]
    table = dict(zip(c, c_data))
    print(json.dumps(table, sort_keys=True, indent=4))

# Вопрос
q = int(input('V1 > ? | >> '))
vi = 'V1'
for i in range(1, n + 1):
    if table['C' + str(i)][vi] > q: print(table['C' + str(i)])

q2 = int(input('V2 == ? | >> '))
vi2 = 'V2'
for i in range(1, n + 1):
    if table['C' + str(i)][vi2] == q2: print(table['C' + str(i)])

q = int(input('\nV1 > ? | >> '))
q2 = int(input('+ V2 < ? | >> '))
for i in range(1, n + 1):
    if (table['C' + str(i)][vi2] < q2) and (table['C' + str(i)][vi] > q): print(table['C' + str(i)])