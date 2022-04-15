import json as jn

def sort_key(t):
    return t[1]


st = input('mega text input in str /w spaces >> ')
dic = dict()
for w in sorted(st.split(), reverse=True):
    if dic.get(w.lower(), 'None') == 'None':
        dic[w.lower()] = 1
    else: dic[w.lower()] += 1

dic = dict(reversed(sorted(dic.items(), key=sort_key)))
print(jn.dumps(dic, indent=2))