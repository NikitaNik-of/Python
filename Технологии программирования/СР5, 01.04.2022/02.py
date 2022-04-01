n = int(input('n >> '))
cities = {input(f'#{_} str >> ') for _ in range(n)}
lenol = len(cities)
check = input('#control str >> ')
cities.add(check)
if lenol == len(cities):
    print('REPEAT')
else:
    print('OK')
