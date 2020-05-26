primetest = 2
bignumber = int(input("Pleasy enter a big number (smaller than yo momma)"))
print("   Bignumber = " + str(bignumber))
biggestprimefactor = 0
while bignumber > 2:

    primeflag = True
    for x in range(2, primetest):
        if primetest % x == 0:
            primeflag = False
            break

    if primeflag:
        # print(str(primetest) + " is a prime number")
        if bignumber % primetest == 0:
            bignumber = bignumber / primetest
            print("newBignumber = " + str(bignumber))
            if primetest > biggestprimefactor:
                biggestprimefactor = primetest
            primetest = 1

    primetest += 1

print("This is the biggest prime factor: " + str(biggestprimefactor))
