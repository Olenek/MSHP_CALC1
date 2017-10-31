def str_showcenter():
    print("\nВведите строку: ")
    s = input()
    width = 80
    a = len(s)
    b = (width - a) // 2
    center = b * ' ' + s + b * ' '
    print(center)
