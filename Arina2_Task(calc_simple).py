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
