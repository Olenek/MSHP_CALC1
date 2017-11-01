def calc_10_2(dex = "a"):
    if (dex == "a"):
        print("Введите 10-чное число:")
        dex = int(input())
    bin = 0
    num = 0
    while dex != 0:
        bin = bin + 10 ** num * (dex % 2)
        dex = dex // 2
        num += 1
    print(bin)