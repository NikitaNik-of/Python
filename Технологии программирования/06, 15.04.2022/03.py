import json as jn

s = input('str key:value \w spaces> ')
dic = dict([(int(w.split(':')[0]), w.split(':')[1]) for w in s.split()])

print(jn.dumps(dic, sort_keys=True, indent=2))