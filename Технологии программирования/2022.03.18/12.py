s1 = input('str of int (1) > ')
s2 = input('str of int (2) > ')
st = {ch for ch in s1 + s2 if ch.isdigit()}
if len(st) == 10 : print('Pag')
else : print('не Pag')