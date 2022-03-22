s = input('str 3 words > ')
lt = [{ch for ch in s.split()[w]} for w in range(3)]
if lt[0] == lt[1] == lt[2] : print('Pag')
else : print('не Pag')