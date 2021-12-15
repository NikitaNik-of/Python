import os
import random

def fileRandom(fp):
    names = ['Иван Иванович Карасев', 'Горацио Дмитриевич Дримов', 'Влад Владимирович Фоксеев', 'Анна Геннадьевна Мисува', 'Никита Анатольевич Титаников', 'Wilbur Soot Sandman']
    if not(os.path.isfile(fp)):
        f = open(fp, 'tw', encoding='utf-8')
        f.close()
    num = random.randint(1,10)
    file_data = []
    for i in range(num):
        person = []
        person.append(names[random.randint(0,5)])
        person.append(random.randint(1,5) * 10 + random.randint(1,6))
        luckyone = random.randint(0, 3)
        if luckyone == 3:
            person.append('5.0 ' * 4)
        else:
            person.append(round(random.randint(2,4) + random.randint(0,99) * 0.01, 2))
            person.append(round(random.randint(2,4) + random.randint(0,99) * 0.01, 2))
            person.append(round(random.randint(2,4) + random.randint(0,99) * 0.01, 2))
            person.append(round((person[2] + person[3] + person[4]) / 3, 2))
        file_data.append(' '.join(map(str, person)) + ' \n')
    with open(fp, 'w', encoding='utf-8') as f:
        f.writelines(file_data)
        
            
def fileRead(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        return [[str(num) for num in line.split()] for line in f]


def samoZachet(lt):
    for i in range(len(lt)):
        if float(lt[i][7]) >= 4:
            print(', '.join(lt[i]))
    print()


def sort(lt):
    for step in range(len(lt)):
        min = step
        for i in range(step + 1, len(lt)):
            if lt[i][7] < lt[min][7]:
                min = i
        (array[step], array[min]) = (array[min], array[step])
    print(array)        


file_path = "C://test.txt"

fileRandom(file_path)
array = fileRead(file_path)

samoZachet(array)
sort(array)
