import math


def calc_simple():
    print("Введите первое число")
    a = int(input())
    print("Введите второе число")
    b = int(input())
    print("Введите операцию")
    c = input()
    if c == "+":
        print(a + b)
    if c == "-":
        print(a - b)
    if c == "/":
        if (a == 0) | (b == 0):
            print("Error")
        else:
            print(a / b)
    if c == "*":
        print(a * b)


def calc_extended():
    print("Введите операцию, если 1 - возведение в степень, 2 - остаток от деления, 3 - нахождение корня")
    a = int(input())
    if a == 1:
        b = int(input())
    c = int(input())
    print(math.pow(b, c))
    if a == 2:
        b = int(input())
    c = int(input())
    print(b % c)
    if a == 3:
        b = int(input())
    print(math.sqrt(b))


def calc_degrees():
    print("Если вы хотите получить sin() угла, то введите 1. Если хотите получить cos() угла, то введите 2.")
    choice = int(input())
    if choice == 1:
        print("Введите угол в градусах:")
        corner = int(input())
        return math.sin(corner)
    elif choice == 2:
        print("Введите угол в градусах:")
        corner = int(input())
        return math.cos(corner)
    else:
        print("Вы ввели не то число.")
        return calc_degrees()


def calc_radians():
    print("Если вы хотите получить sin() угла, то введите 1. Если хотите получить cos() угла, то введите 2.")
    choice = int(input())
    if choice == 1:
        print("Введите угол в радианах:")
        corner = int(input())
        corner *= 180/math.pi
        return math.sin(corner)
    elif choice == 2:
        print("Введите угол в радианах:")
        corner = int(input())
        corner *= 180/math.pi
        return math.cos(corner)
    else:
        print("Вы ввели не то число.")
        return calc_radians()


def check_brackets(s = 0):
    if s == 0:
        print("Введите строчку с формулой: ")
        s = input()
    bracket1 = 0
    bracket2 = 0
    for x in s:
        if x == '{':
            bracket1 += 1
        elif x == '}':
            bracket2 += 1
    if bracket1 == bracket2:
        print("ДА")
        return True
    print("НЕТ")
    return False


def menu_numbers():
    print("Введите номер операции, которую вы хотите соверишть: ",
          "1.Простые операции",
          "2.Расширенные операции",
          "3.Тригонометрические действия с градусами",
          "4.Тригонометрические действия с радианами",
          "5.Логические операции",
          "6.Перевод в различные СС",
          "7.Проверка скобок")
    a = input()
    if a == 1:
        print(calc_simple())
    if a == 2:
        print(calc_extended())
    if a == 3:
        print(calc_degrees())
    if a == 4:
        print(calc_redians())
    if a == 5:
        print(calc_logic())
    if a == 6:
        print(menu_logic())
    if a == 7:
        print(check_brackets())
