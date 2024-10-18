from time import time

def wheelFactorization(num):
    if num < 2:
        return False
    elif num in (2, 3, 5, 7):
        return True
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        return False
    for i in range(11, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def findLargestPrimeWF(limit_time):
    start_time = time()
    num = 3 # Start from a large number
    largest_prime = 2
    count = 1
    while time() - start_time < limit_time:
        if wheelFactorization(num):
            largest_prime = num
            count += 1
        num += 1
    
    return largest_prime, count


# timelimit = 60
# largest_prime_wheel = find_largest_prime_wheel(timelimit)
# print("Largest prime (Wheel Factorization):", largest_prime_wheel)
#999999973043
