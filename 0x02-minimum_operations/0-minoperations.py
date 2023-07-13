#!/usr/bin/python3
"""
Calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""

def minOperations(n):
    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
