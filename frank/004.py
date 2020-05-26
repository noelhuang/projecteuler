# print(max([x * y for x in range(100, 100000) for y in range(100, 100000) if str(x * y) == str(x * y)[::-1]]))

m = -1
n = 1000
for x in range(n):
    for y in range(n):
        if x * y > m and str(x * y) == str(x * y)[::-1]:
            m = x * y

if m >= 0:
    print("The larges palindrome is " + str(m))
else:
    print("We found nothing")
