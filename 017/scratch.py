lst19 = [i for i in range(1, 10)]

print(lst19)


def check(lst, a):
    for i in range(0, len(lst)):
        if lst[i] == a:
            return True
    return False


print(check(lst19, 5))
