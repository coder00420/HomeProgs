def get_primes(n):
    sieve = [False if i % 2 == 0 else True for i in range(n)]
    primes = [2]
    for p in range(3, n, 2):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n, p * 2):
                sieve[i] = False
    return primes

range_ = int(input()) + 1
numbers = list(range(1, range_))
primes = get_primes(range_)
boxes = [[]]
for n in numbers:
    n_dividers = []
    for prime in primes:
        if prime > n:
            break
        if prime % x == 0:
            n_dividers.append(prime)
    n_dividers = (n, n_dividers)
    for box in boxes:
        if not(box):
            box.append(n_dividers)
            break
        for number in box:
            breaking = False
            for prime in n_dividers[1]:
                if prime in number[1]:
                    breaking = True
                    break
            if breaking == True:
                break
        #else: