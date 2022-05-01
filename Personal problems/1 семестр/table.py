import os
import random
import time

from numpy import sort


def fileRandom(fp):
    names = ['Иван Иванович Карасев', 'Горацио Дмитриевич Дримов', 'Влад Владимирович Фоксеев',
             'Анна Геннадьевна Мисува', 'Никита Анатольевич Титаников', 'Wilbur Soot Sandman']
    if not (os.path.isfile(fp)):
        f = open(fp, 'tw', encoding='utf-8')
        f.close()
    num = random.randint(100, 500)
    file_data = []
    for i in range(num):
        person = []
        person.append(names[random.randint(0, 5)])
        person.append(random.randint(1, 5) * 10 + random.randint(1, 6))
        luckyone = random.randint(0, 3)
        if luckyone == 3:
            person.append('5.0 ' * 3)
        else:
            person.append(round(random.randint(2, 4) + random.randint(0, 99) * 0.01, 2))
            person.append(round(random.randint(2, 4) + random.randint(0, 99) * 0.01, 2))
            person.append(round(random.randint(2, 4) + random.randint(0, 99) * 0.01, 2))
            # person.append(round((person[2] + person[3] + person[4]) / 3, 2))
        file_data.append(' '.join(map(str, person)) + ' \n')
    with open(fp, 'tw', encoding='utf-8') as f:
        f.writelines(file_data)


def fileRead(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        return [[str(num) for num in line.split()] for line in f]


def samoZachet(lt, fp):
    f = open(fp, 'tw', encoding='utf-8')
    f.write('1. Средний балл >4:\n\n')
    for i in range(len(lt)):
        mid = (float(lt[i][6]) + float(lt[i][5]) + float(lt[i][4])) / 3
        if mid >= 4:
            f.write(' '.join(lt[i]) + '\n')
    f.write('\n')


def select_sort(lt, fp):
    s_time = time.time_ns()
    mid = [round((float(lt[i][6]) + float(lt[i][5]) + float(lt[i][4])) / 3, 2) for i in range(len(lt))]
    for step in range(len(lt)):
        min = step
        for i in range(step + 1, len(lt)):
            if mid[i] < mid[min]:
                min = i
        (lt[step], lt[min]) = (lt[min], lt[step])
        (mid[step], mid[min]) = (mid[min], mid[step])
    with open(fp, 'a', encoding='utf-8') as f:
        f.write('\n2. Сортировка Selection sort:\n\n')
        for i in range(len(lt)):
            f.write(' '.join(lt[i]) + '\n')
    print(time.time_ns() - s_time)


def def_sort(lt, fp):
    s_time = time.time_ns()
    mid = [(round((float(lt[i][6]) + float(lt[i][5]) + float(lt[i][4])) / 3, 2), i) for i in range(len(lt))]
    mid.sort()
    with open(fp, 'a', encoding='utf-8') as f:
        f.write('\n3. Сортировка default sort:\n\n')
        for i in mid:
            f.write(' '.join(lt[i[1]]) + '\n')
    print(time.time_ns() - s_time)

file_path = "C://test.txt"
output_path = "C://output.txt"

fileRandom(file_path)
array = fileRead(file_path)

samoZachet(array, output_path)
select_sort(array.copy(), output_path)
def_sort(array.copy(), output_path)
