#!/usr/bin/env python
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

def getPrimeFactors(n):
    result = []

    while n % 2 == 0:
        result.append(2)
        n //= 2

    max = math.sqrt(n+1)
    i = 3
    while i <= max:
        if n % i is 0:
            result.append(i)
            n //= i
            max = math.sqrt(n+i)
        else:
            i += 2
    if n is not 1:
        result.append(n)

    return result
import time
start_time = time.time()
print max(getPrimeFactors(600851475143))
print("--- Completed in %s seconds ---" % (time.time() - start_time))
