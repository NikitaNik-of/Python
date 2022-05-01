import os
import subprocess as sp
from tokenize import blank_re


def fileMake(fp):
    if not(os.path.isfile(file_path)):
        f = open(file_path, 'tw', encoding='utf-8')
        f.close()
    print("\n\nЯ специально создал для вас файл, для удобного ввода матрицы.\nПожалуйста, введите квадратную матрицу, между элементами в строке - пробел, между столбцами - красная строка!")
    sp.Popen(["notepad.exe", fp])
    ans = input(
        "Как только будете готовы, напишите Y, если хотите завершить программу - N >>")
    if ans == "N" or ans == "n":
        os.abort()


def fileRead(fp):
    with open(fp, 'r') as f:
        try:
            return [[int(num) for num in line.split(' ')] for line in f]
        except ValueError:
            print("\nОшибка чтения файла!\nНеверный формат данный при преобразовании в число. Программа завершилась.\n\n")
            os.abort()


def det(ar, t):
    ad = []
    if len(ar) == 1:
        return ar[0][0], [ar[0][0]]
    else:
        s = 0
        for i in range(len(ar)):
            a = ar[0][i]
            mt = [[ar[k][j] for k in range(len(ar)) if k > 0]
                  for j in range(len(ar)) if j != i]
            if i % 2 == 0:
                d, emp = det(mt, 1)
                s += a * d 
                if t == 0:
                    ad.append(d)
            else:
                d, emp = det(mt, 1)
                s -= a * d
                if t == 0:
                    ad.append(d * -1)
        return s, ad


file_path = "C://test.txt"
b = False
fileMake(file_path)
mat = fileRead(file_path)

for i in range(len(mat)):
    if len(mat) != len(mat[i]):
        b = True
if b:
    print("\nВы неверно ввели матрицу. Пожалуйста перепроверьте написание и пробелы, иначе пожалуйтесь на баг)\nПрограмма завершилась.\n\n")
else:
    dt, algdop =  det(mat, 0)
    print("\nДетерминант матрицы:", dt, end="")
    print("\nАлгебраические дополнения для первой строки:", algdop, end="\n\n")


# n = int(input("Матрица N x N: Введите n (int) >> "))
# mat = [[int(input("Введите элементы матрицы: [" + str(j) + "," + str(i) + "] >> ")) for j in range(n)] for i in range(n)]
# print("\nДетерминант матрицы:", det(mat))
