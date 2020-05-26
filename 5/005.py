divflag = False

for x in range(100000000):
    for y in range(1, 21):
        if x % y == 0:
            divflag = True
        else:
            divflag = False
            break

    if divflag:
        print(x)