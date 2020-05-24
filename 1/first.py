limit = int(input("Calculate the sum of all multiples of 3 and 5 below (please enter a number): "))  # The upper
# limit is defined here
n3 = (limit-1) // 3  # The number of multiples of 3 below the limit is calculated here
n5 = (limit-1) // 5  # The number of multiples of 5 below the limit is calculated here
print("The number of multiples of 3 below " + str(limit) + " is equal to " + str(n3))
print("The number of multiples of 5 below " + str(limit) + " is equal to " + str(n5))

sum3 = 0  # We need a variable to use later in the loop to be able to do the summation of all multiples
for x in range(1, n3 + 1):  # We select the range of x to be 333 (which is the number of multiples)
    x = x * 3   # Here we find all multiples of 3 by multiplying the previously defined range with 3, and assign it to x
    sum3 = sum3 + x   # Here we sum up all multiples of 3 below 1000
print("The sum of all multiples of 3 below the limit is equal to:")
print(sum3)   # Here we print the final value of the sum of all multiples of 3 below 1000


sum5 = 0  # We need a variable to use later in the loop to be able to do the summation of all multiples
for x in range(1, n5 + 1):  # We select the range of x to be 199 (which is the number of multiples)
    x = x * 5   # Here we find all multiples of 3 by multiplying the previously defined range with 3, and assign it to x
    sum5 = sum5 + x   # Here we sum up all multiples of 3 below 1000
print("The sum of all multiples of 5 below the limit is equal to:")
print(sum5)   # Here we print the final value of the sum of all multiples of 3 below 1000

sumtotal = sum3 + sum5
print("The sum of all multiples of 3 and 5 below " + str(limit) + " is equal to: ")
print(sumtotal)

#faster solution: sum(x for x in range(limit) if (x % 3 == 0 or x % 5 == 0))