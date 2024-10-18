from time import time
import random

def millerRabin(n, k=5):
    if n <= 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def findLargestPrimeMR(limit_time):
    start_time = time()
    num = 2  
    largest_prime = 2
    count = 0
    while time() - start_time < limit_time:
        if millerRabin(num):
            largest_prime = num
            count += 1
        num += 1
    
    return largest_prime, count
#999996401473
# timelimit = 60
# largest_prime_miller_rabin = find_largest_prime_miller_rabin(timelimit)
# print(f"Largest prime (Miller-Rabin): {largest_prime_miller_rabin}")
