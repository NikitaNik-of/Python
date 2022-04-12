colors = [s for s in input("Colors /w spaces >>").split()]
dick = dict(zip(range(1, len(colors) + 1), colors))
# new_dic = dict()
# for k in dick.keys():
#     if dick(k) != 'None': 
print(dick)
new_dic = {key:dick[key] for key in dick.keys() if dick[key] != 'None'}

print(new_dic)