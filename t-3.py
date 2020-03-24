import math


def prime_factorization(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        while x % i == 0:
            print(i)
            x /= i

    if x != 1:
        print(x)


prime_factorization(44)
