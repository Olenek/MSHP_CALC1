import math


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
