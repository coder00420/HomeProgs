import math
def get_prime_numbers(n):
    primes_row = [True for _ in range(n)]
    primes_row[0] = False
    i = 1
    while i <= math.isqrt(n):
        if primes_row[i] == False:
            i += 1
            continue
        j = i * 2 + 1
        while j <= n - 1:
            primes_row[j] = False
            j += i + 1
        i += 1
    primes = [_ + 1 for _ in range(n) if primes_row[_] == True]
    return primes