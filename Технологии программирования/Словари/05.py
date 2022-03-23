from numpy import NaN


n = int(input('int > '))
dics = [dict(zip(['name', 'phone', 'email'], input(f' #{_ + 1} | name phone email > ').split())) for _ in range(n)]
dics = sorted(dics, key=lambda dic: dic['name'])
for i in range(n):
    if 'email' not in dics[i]:
        print(f'Имя: {dics[i].get("name", "Отсутсвует")}, Номер: {dics[i].get("phone", "Отсутсвует")}')