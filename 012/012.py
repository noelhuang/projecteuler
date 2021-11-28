trianglenumbers = []

naturalnumbers = [i for i in range(1, 100001)]

# print(naturalnumbers)

listpos = 0

trianglenumber = 0

# Below we calculate a trianglenumber, by adding the next natural number to the previous already existing trianglenumber
# The value of the triangle number is updated by '+=', then the trianglenumbers list is updated via .append
# The list position is then increased by 1
while listpos < 100000: # Fill in here the max trianglenumber you want to have
    trianglenumber = trianglenumber + naturalnumbers[listpos]
    trianglenumbers.append(trianglenumber)
    listpos += 1

print(trianglenumbers)

flag = 1

for n in range(10000, 100000):
    trianglenumber = trianglenumbers[n]
    divisors = 1
    if flag == 2:
        break
    for i in range(1, trianglenumber//2+1):
        if trianglenumber % i == 0:
            divisors += 1
            if divisors > 500:
                print(f"This is trianglenumber with 500 div:{trianglenumber}")
                flag = 2
                break
            if flag == 2:
                break
            else:
                print(divisors)
