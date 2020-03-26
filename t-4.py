import math

# A function to print all prime factors of
# a given number n


def primeFactors(n):

    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2),
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            print(i),
            n = n / i

    # Condition if n is a prime
    # number greater than 2 fsdaf
    if n > 2:
        print(n)


def prime_factorization(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        while x % i == 0:
            print(i)
            x /= i

    if x != 1:
        print(x)


primeFactors(60085147514)


def hbstuff():
    num = 600851475
    prime = False

    while prime is False:
        for number in range(2, num):
            prime = True
            if num % number == 0:
                prime = False
                x = number
                num = int(num / x)
                break
    print(num)


hbstuff()
