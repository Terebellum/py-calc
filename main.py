s = 1
while s:
    a = int(input("Input number a: "))
    b = int(input("Input number b: "))
    c = input("Choose an operation (+/-/*/:)")
    if c == "+":
        print(a, c, b, "=", a+b)
    elif c == "-":
        print(a, c, b, "=", a-b)
    elif c == "*":
        print(a, c, b, "=", a*b)
    elif c == ":":
        print(a, c, b, "=", a/b)
    else:
        print("Undefined operation")
    while 1:
        r = input("One more loop(y/n)? ")
        if r == "y":
            break
        elif r == "n":
            s = 0
            break
        else:
            print("Wrong action")
