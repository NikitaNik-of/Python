s = input('str of ints > ')
st = {int(i) for i in s.split()}
for num in s.split():
    if int(num) in st: print(f' {num} : Не было')
    else: print(f' {num} : Было')
    st.discard(int(num))