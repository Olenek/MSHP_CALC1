def str_words():
    string = input("Введите строку:\n")
    print(len(string), len(list(string.split())))

def str_simple():
    print('Выберите действие:')
    inp = input()
    if inp == '+':
        print('Введите первую строку:')
        s1 = input()
        print('Введите вторую строку:')
        s2 = input()
        print('Ответ:', s1+s2)
    elif inp == '*':
        print('Введите строку:')
        s = input()
        print('Введите множитель:')
        n = int(input())
        print('Ответ:', s*n)
    else: print('Ошибка: неверное действие. Попробуйте снова...') & str_simple()

def str_showcenter():
    print("\nВведите строку: ")
    s = input()
    width = 80
    a = len(s)
    b = (width - a) // 2
    center = b * ' ' + s + b * ' '
    print(center)

def menu_settings():
    print('Выберите действие:')
    print('1. Простые операции со строками')
    print('2. Вывод строки по центру экрана')
    print('3. Количество слов и количество символов')
    ent = int(input())
    if ent == 1:
        str_simple()
    elif ent == 2:
        str_showcenter()
    elif ent == 3:
        str_words()
    else: print('Ошибка: неверное действие. Попробуйте снова...') & menu_settings()

menu_settings()