import json as jn

s = input('str 1 key:value \w spaces> ')
dic = dict()
for _ in s.split():
    st = _.split(':')
    dic[st[0]] = int(st[1])

s = input('str 2 key:value > ')
dic2 = dict()
for _ in s.split():
    st = _.split(':')
    dic2[st[0]] = int(st[1])

for key in dic2.keys():
    if key not in dic: dic[key] = dic2[key]
    else: dic[key] -= dic2[key]

print(jn.dumps(dic, sort_keys=True, indent=2))

