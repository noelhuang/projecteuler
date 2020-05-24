primetest = 2
primeflag = False
bignumber = int(input("Pleasy enter a big number (smaller than yo momma)"))
print("   Bignumber = " + str(bignumber))
biggestprimefactor = 0
while bignumber != 1:
    primetest += 1

    for x in range(2, primetest):
        if primetest % x == 0:
            primeflag = False
            break
        else:
            primeflag = True

    if primeflag:
        #print(str(primetest) + " is a prime number")
        if bignumber % primetest == 0:
            bignumber = bignumber / primetest
            print("newBignumber = " + str(bignumber))
            if primetest > biggestprimefactor:
                biggestprimefactor = primetest
            primetest = 2
            continue
        else:
            continue

    else:
        #print(str(primetest) + " is not a prime number")
        primeflag = False

print("This is the biggest prime factor: " + str(biggestprimefactor))
