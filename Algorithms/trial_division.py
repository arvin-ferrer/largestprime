#TRIAL DIVISION ALGORITHM

from time import time

def trialDivision(n):
    if n < 2:
        return False
    for i in range(2, n): #STARTED AT 2 BECAUSE IT'S THE SMALLEST PRIME NUMBER
        if n % i == 0:
            return False
    return True

def findlargestPrime(limit):
    start_time = time()
    count = 0
    largest_prime = 2
    num = 2
    while time() - start_time < limit:
        if trialDivision(num):
            largest_prime = num
            count += 1
        num += 1

    return largest_prime, count

def optimizedtrialDivision(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2)) + 1):  # Start checking from 2
        if n % i == 0:
            return False
    return True

def optimizedfindlargestPrime(limit):
    start_time = time()
    largest_prime = 2
    count_of_primes = 0  # Initialize the counter for prime numbers
    num = 2
    
    while time() - start_time < limit:
        if optimizedtrialDivision(num):
            largest_prime = num  # Update largest prime
            count_of_primes += 1  # Increment the prime count
        num += 1
    
    return largest_prime, count_of_primes  # Return both values

    
# timelimit = 5 #CHANGE THIS VALUE IF YOU WANT TO INCREASE THE TIME LIMIT 
# largest_prime = findlargestPrime(timelimit)
#4191709

# print(f"Largest prime (Trial Division): {largest_prime}")
