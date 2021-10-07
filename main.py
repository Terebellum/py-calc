s = 1
while s:
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    c = input("Выберите знак(+/-/*/:)")
    if c == "+":
        print(a, c, b, "=", a+b)
    elif c == "-":
        print(a, c, b, "=", a-b)
    elif c == "*":
        print(a, c, b, "=", a*b)
    elif c == ":":
        print(a, c, b, "=", a/b)
    else:
        print("Неизвестный знак")
    while 1:
        r = input("Хотите продолжить пользоваться программой(y/n)? ")
        if r == "y":
            break
        elif r == "n":
            s = 0
            break
        else:
            print("Неправильный ввод")
