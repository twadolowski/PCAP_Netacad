c0 = int(input("Enter a non-negative and non-zero integer: "))
if c0 > 0:
    steps = 0
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 / 2
        else:
            c0 = 3 * c0 + 1
        print(int(c0))
        steps += 1
    print("steps =", steps)
else:
    print("Bad input!")
