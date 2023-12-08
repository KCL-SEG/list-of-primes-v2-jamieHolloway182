"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError('Work with Positive Numbers Only')
    list = [2]
    count = 3
    while (len(list) < number_of_primes):
        isPrime = True
        for i in range(2, math.floor(count / 2)):
            if count % i == 0:
                count += 2
                isPrime = False
                break
        if isPrime:
            list.append(count)
            count += 2
    return list

