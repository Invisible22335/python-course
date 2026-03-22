n = int(input())

if n <= 0:
    print("Неверный ввод")
else:
    #двоичная система
    a = ""
    x = n
    while x > 0:
        a = str(x % 2) + a
        x = x // 2

    #восьмеричная система
    b = ""
    x = n
    while x > 0:
        b = str(x % 8) + b
        x = x // 8

    #шестнадцатеричная система
    c = ""
    x = n
    digits = "0123456789ABCDEF"
    while x > 0:
        c = digits[x % 16] + c
        x = x // 16

    print(a, b, c)