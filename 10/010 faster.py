#   The brute force method used earlier to check for primes is too slow, so...
#   We now use the sieve of Eratosthenes
primesum = 0
numlist = []

count = 0
while count < 2000000:
    numlist.append(False)
    count += 1
print(numlist)

for i in range(2,2000001):
    if numlist[i-1] == False:
        primesum = primesum + i
        numlist[i-1] = i
    for x in range(2, int(2000000/i+1)):    # The upper range in this line is weird
        numlist[i*x-1] = i*x

print(primesum)


print(numlist)

# maxprime = 10
# primelist = [True for _ in range(2, maxprime+1)]
# print(primelist)
#
# for n in range(2, maxprime+1):
#     if primelist[n]:
#         if 2*n < maxprime+1:
#             primelist[2*n: maxprime+1: n] = False
#         else:
#             primelist[n] = False
#
# print(primelist)

# usedlist = [False, False]
# m = 1
# j = 1
#
# # Loop for all numbers up to maxprime
# # Take the square root as upper limit, because all numbers above the square root will be primes if they are not marked
# for n in range(3, int(maxprime**0.5)):
#
#     if bool(usedlist[n]) == False:
#         usedlist.append(True)
#         for x in range(1,int(maxprime//n+1)):
#             if usedlist[n*x] == False:
#                 usedlist.append(n * x)
#
# for i in range(int(maxprime**0.5), maxprime):
#
#     if usedlist.count(i) == 0:
#         primelist.append(i)
#         print(primelist[-1])
#
#
# print(primelist)
# print(usedlist)
# print(sum(primelist))