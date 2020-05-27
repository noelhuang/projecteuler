divflag = False
found = False
x = 1
while not found:
    for y in range(1, 11):
        if x % y == 0:
            divflag = True
        else:
            divflag = False
            break

    if divflag:
        if x != 0:
            print(x)
            found = True
            break

    x += 1
