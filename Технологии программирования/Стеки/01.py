stack = []
t = 0
while True:
    if t > 50:
        print('Ты надоел спамить, не буду ничего делать(')
    if len(stack) > 0:
        print('Текущий стек:', stack)

    queue = input('\nОжидание команды >> ')
    ql = [i.lower() for i in queue.split()]

    if len(ql) == 0:
        continue
    elif ql[0] == 'push':
        if len(ql) > 2:
            t += 1
            print('Лишние данные для команды push!')
        elif len(ql) < 2:
            t += 1
            print('Введите число для команды push!')
        else:
            try:
                stack.append(int(ql[1]))
                print('Добавлен элемент {ql[1]} в стек')
            except ValueError:
                print('Ошибка: ValueError')
    elif ql[0] == 'pop':
        if len(ql) > 1:
            t += 1
            print('Лишние данные для команды pop!')
        elif len(stack) == 0:
            t += 1
            print('Стек уже пустой!')
        else:
            stack.pop()
            print('Убран последний элемент в стеке')
    elif ql[0] == 'back':
        if len(ql) > 1:
            t += 1
            print('Лишние данные для команды back!')
        else:
            print('Последний элемент в стеке:', stack[-1])
    elif ql[0] == 'size':
        if len(ql) > 1:
            t += 1
            print('Лишние данные для команды size!')
        else:
            print('Количество элементов в стеке:', len(stack))
    elif ql[0] == 'clear':
        if len(ql) > 1:
            t += 1
            print('Лишние данные для команды clear!')
        else:
            stack = []
            print('Стек очищен!')
    elif ql[0] == 'exit':
        print('Пока-пока!')
        break