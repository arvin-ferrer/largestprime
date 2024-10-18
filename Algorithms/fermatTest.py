from time import time
import random

def fermatPrimality(n, k=5):
    if n <= 1:
        return False
    elif n == 2:
        return True
    for _ in range(k):
        a = random.randint(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def largestPrimeFermat(limit_time):
    start_time = time()
    num = 3  # Start from 3 (smallest odd prime greater than 2)
    largest_prime = 2  # Initialize with 2 as the first prime
    count = 1  # Count includes the first prime (2)

    # Store primes for later validation
    primes = [2]

    while time() - start_time < limit_time:
        if fermatPrimality(num):
            count += 1
            largest_prime = num  # Update largest prime
            primes.append(num)   # Track prime numbers found

            # Ensure consistency: if count matches the prime number, exit
            if count == largest_prime:
                break
        num += 2  # Skip even numbers
    
    # Ensure consistency between nth prime and total primes found
    nth_prime = primes[count - 1]  # Get the nth prime based on the count

    return nth_prime, count



# timelimit = 60
# largest_prime_fermat = find_largest_prime_fermat(timelimit)
# print("Largest prime (Fermat):", largest_prime_fermat)
