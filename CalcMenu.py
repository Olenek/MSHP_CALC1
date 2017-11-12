def get_action():
    t = int(input('Введите номер действия: '))
    while t not in [1, 2, 3]:
        t = int(input('Некорректно, введите ещё раз: '))
    return t
def print_num_menu(num):
    if num == 1:
        print(number_ops)
    elif num == 2:
        print(string_ops)
    elif num == 3:
        print(long_ops)
def menu():
    help()
    num = get_action()
    print_num_menu(num)
def help():
    print('1 - Калькулятор чисел\n2 - Калькулятор строк\n3 - Длинная арифметика')
def main():
    input('Приветствую вас, Хозяин.\nДля перехода в калькулятор нажмите на любую клавишу...')
    menu()
main()