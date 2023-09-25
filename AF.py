import math

while True:
    print("please input the values of a, b and c ")

    while True:
        a = (input("a: "))
        a = float(a)
        if a <= 0 or a >= 0:
            print("Input 'b'")
            break
        else:
            print("Please type numbers only!")

    while True:
        b = (input("b: "))
        b = float(b)
        if b <= 0 or b >= 0:
            print("Input 'c'")
            break
        else:
            print("Please type numbers only!")

    while True:
        c = (input("c: "))
        c = float(c)
        if c <= 0 or c >= 0:
            print("Solution")
            break
        else:
            print("Please type numbers only!")

    r = (b ** 2 - (4 * a * c))

    if r < 0:
        print("Complex equation!")
    else:
        r = float(r)
        root = math.sqrt(r)

        x1 = (-b + float(root)) / 2 * a
        x2 = (-b - float(root)) / 2 * a
        print(f"x = {x1} and {x2}")
    done = input("Do you want to quit? ")
    if done.lower() == "yes" or "y":
        print("Goodbye")
        break
    elif done.lower() == "no" or "n":
        continue
    else:
        print("invalid")