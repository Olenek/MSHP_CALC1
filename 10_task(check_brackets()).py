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