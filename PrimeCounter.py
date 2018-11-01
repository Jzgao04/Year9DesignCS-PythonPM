intN = int(input())
# Print the number of prime numbers less than N
# i.e if N = 10, then the output should be 4 //2 3 5 7
intPrimeCount = 0 #Count the number of prime numbers less than intN
for i in range(1, intN):
    #Let them check each time whether is is prime
    intFactor = 0 #count the number of factors of i
    for j in range(1, i+1):
        if(i % j == 0): 
            intFactor = intFactor + 1
    if intFactor == 2:
        intPrimeCount = intPrimeCount + 1

print("There are" , intPrimeCount, "numbers less than", intN, "are primes")