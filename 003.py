import math
import sys

def next_prime(primes):
    next = primes[-1]
    while 1:
        is_prime = True
        next = next + 2
        for i in primes:
            if next % i == 0:
                is_prime = False
                break
        
        if is_prime: return next

N = 600851475143
square = int(math.sqrt(N))
primes = [3]

while N > 1:
    prime = primes[-1]
    while N % prime == 0:
        N /= prime
    primes.append(next_prime(primes))

print(prime)
