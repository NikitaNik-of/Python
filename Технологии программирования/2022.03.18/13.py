s1 = input('str of int (1) > ')
s2 = input('str of int (2) > ')

st1 = {ch for ch in s1 if ch.isdigit()}
st2 = {ch for ch in s2 if ch.isdigit()}

if st1 == st2 : print('Pag')
else : print('не Pag')