divflag = False

for x in range(10000000):
    for y in range(1,11):
        if x % y == 0:
            divflag = True
        else:
            divflag = False
            break

    if divflag:
        if x != 0:
            print(x)
            break