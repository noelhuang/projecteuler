a = 1
b = 1
for a in range(1000):
    for b in range(1000):
        c = (a**2 + b**2)**0.5
        if c % 1 == 0:
            if a + b + c == 1000:
                print("a=" +str(a) + " b=" + str(b) + " c=" + str(c))
                print("product = " + str(a*b*c))
                break