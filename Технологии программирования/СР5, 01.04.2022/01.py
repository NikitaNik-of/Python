s = input('str > ')
st = {ch for ch in s}
if len(s) == len(st) : print("Pag! (без повторов)")
else : print("Не pag( (с повторами)")
