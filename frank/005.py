def get_number(x):
    found = False
    i = 1
    while not found:
        if get_flag(i, x):
            return i
        i += 1


def get_flag(i, x):
    for j in range(1, x):
        if i % j != 0:
            return False
    return True


print(get_number(21))
