def method1():
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


def method2(x):
    found = False
    i = 1
    while not found:
        if getFlag(i, x):
            return i
        i += 1


def getFlag(i, x):
    for j in range(1, x):
        if i % j != 0:
            return False
    return True


print(print(method2(21)))
