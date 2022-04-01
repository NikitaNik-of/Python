marks = {n + 1 for n in range(10)}
stud1 = {marks.discard(int(ch)) for ch in input('#1 | ints /w spaces >> ').split()}
stud2 = {marks.discard(int(ch)) for ch in input('#2 | ints /w spaces >> ').split()}
stud3 = {marks.discard(int(ch)) for ch in input('#3 | ints /w spaces >> ').split()}
print('Не было оценок: ', end='')
print(*sorted(marks), sep=', ')