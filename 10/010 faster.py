#   The brute force method used earlier to check for primes is too slow, so...
#   We now use the sieve of Eratosthenes

primelist = []
maxprime = 2000000
usedlist = []
m = 1
j = 1

# Loop for all numbers up to maxprime
# Take the square root as upper limit, because all numbers above the square root will be primes if they are not marked
for n in range(2, int(maxprime**0.5)):

    if usedlist.count(n) == 0:
        primelist.append(n)
        for x in range(1,int(maxprime//n+1)):
            if usedlist.count(n*x) == 0:
                usedlist.append(n * x)

for i in range(int(maxprime**0.5), maxprime):

    if usedlist.count(i) == 0:
        primelist.append(i)
        print(primelist[-1])


print(primelist)
print(usedlist)
print(sum(primelist))