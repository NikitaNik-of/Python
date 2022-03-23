n = int(input('int > '))
dics = [dict(zip(['name', 'phone', 'email'], input(f' #{_ + 1} | name phone email > ').split())) for _ in range(n)]
dics = sorted(dics, key=lambda dic: dic['name'])
for i in range(n):
    if dics[i]['phone'].endswith('1'):
        print(f'Имя: {dics[i].get("name", "Отсутсвует")}, Номер: {dics[i].get("phone", "Отсутсвует")}, E-mail: {dics[i].get("email", "Отсутсвует")}')