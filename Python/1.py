#!/usr/bin/env python
"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time
start_time = time.time()
print sum([num for num in range(1, 1000) if num % 3 is 0 or num % 5 is 0])
print("--- Completed in %s seconds ---" % (time.time() - start_time))
