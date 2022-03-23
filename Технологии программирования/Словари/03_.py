s = input('str key:value > ')
dic = dict()
for _ in s.split():
    st = _.split(':')
    dic[st[0]] = st[1]

print(dic)