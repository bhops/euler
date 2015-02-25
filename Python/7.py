#!/usr/bin/env python
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""
def prime_sieve():
    D = {}
    n = 2
    while True:
        if n not in D:
            yield n
            D[n * n] = [n]
        else:
            for p in D[n]:
                D.setdefault(p + n, []).append(p)
            del D[n]
        n += 1

def nth_prime(n):
    for i, prime in enumerate(prime_sieve()):
        if i == n - 1:
            return prime

import time
start_time = time.time()
print nth_prime(10001)
print("--- Completed in %s seconds ---" % (time.time() - start_time))
