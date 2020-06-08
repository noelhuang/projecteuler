# primecheck
primetest = 3
primeflag = False
primesum = 2    # starts at 2 because it is hard to test if 2 is a prime
while primetest < 100:
    for n in range(2,primetest):
        if primetest % n != 0:
            primeflag = True
        else:
            primeflag = False
            break
    if primeflag:
        primesum += primetest
    primetest += 1

print(primesum)