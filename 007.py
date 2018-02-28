
def next_prime(primes):
    next = primes[-1]
    if next == 2:
        return 3
    while 1:
        is_prime = True
        next += 2
        for i in primes:
            if next % i == 0:
                is_prime = False
                break
        
        if is_prime: return next

primes = [2]
for i in range(1, 10001):
    next = next_prime(primes)
    primes.append(next)

print(primes[-1])
