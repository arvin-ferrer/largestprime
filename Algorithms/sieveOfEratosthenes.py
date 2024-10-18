from time import time

def sieveOfEratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

def findLargestPrimeSOE(limit_time):
    start_time = time()
    limit = 1000  # Start with a reasonable limit
    largest_prime = None
    prime_count = 0  # To count all primes found

    while time() - start_time < limit_time:
        primes = sieveOfEratosthenes(limit)
        if primes:
            largest_prime = primes[-1]  # Update to the last (largest) prime found
            prime_count = len(primes)  # Update the prime count to match total primes found

        if prime_count == largest_prime:  # Check if the largest prime matches the count
            break

        limit *= 2  # Double the limit for the next iteration

    return largest_prime, prime_count
# Return largest prime and total count


# timelimit = 60
# largest_prime_sieve = findlargestPrime(timelimit)
# print(f"Largest prime (Sieve of Eratosthenes): {largest_prime_sieve}")
#163839967