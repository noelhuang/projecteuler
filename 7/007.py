primetest =3
primecount = 2      # Counter for while loop
nth_prime = 10001
while primecount <= nth_prime:
    for x in range(2, primetest):
        if primetest % x == 0:
            primeflag = False
            break
        else:
            primeflag = True
    if primeflag:
        newprime = primetest
        print("This is the new prime: " + str(newprime))
        primecount += 1     # Increase the counter
    primetest += 1      # Increase number to test


print("The nth prime is: " + str(newprime))