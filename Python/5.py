#!/usr/bin/env python
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def divides_by_all(n):
    for i in xrange(1,21):
        if n % i is not 0:
            return False
    return True

def main():
    result = 20
    while not divides_by_all(result):
        result += 20
    return result

import time
start_time = time.time()
print main()
print("--- Completed in %s seconds ---" % (time.time() - start_time))
