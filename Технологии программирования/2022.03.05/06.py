s = input("str > ")
del_ = ''
for ch in {ch for ch in s if not ch.isalpha()}:
    del_ += ch
print(f'Найденные символы: {del_}')
alpha = set((words.strip(del_)).lower() for words in s.split() if len(words.strip(del_)) < 4) 
print(*sorted(alpha), sep = ' ')