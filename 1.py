import math


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