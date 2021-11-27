collatz = []
temp = []

for n in range(1, 1000000):
    temp.append(n)
    while n > 1:
        if n % 2 == 0:
            n = n/2
            temp.append(n)
        else:
            n = 3*n + 1
            temp.append(n)
    if len(temp) > len(collatz):
        collatz = temp
    temp = []

print(temp)
print(f"This is longest collatz chain: {collatz}")
