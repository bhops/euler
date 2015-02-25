#!/usr/bin/env python
"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time
start_time = time.time()
print max(a*b for a in range(100, 1000) for b in range(a, 1000) if str(a*b) == str(a*b)[::-1])
print("--- Completed in %s seconds ---" % (time.time() - start_time))
