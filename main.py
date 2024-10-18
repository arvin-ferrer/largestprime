from Algorithms.trial_division import *
from Algorithms.fermatTest import *
from Algorithms.millerRabinTest import *
from Algorithms.sieveOfEratosthenes import *
from Algorithms.wheelFactorization import *

def menu():
    print("""
    
    Choose a generator        
    
    [1] Trial Division Method   
    [2] Optimized Trial Division Method 
    [3] Sieve of Eratosthenes Method
    [4] Fermat Primality Test
    [5] Wheel Factorization Method
    [6] Miller-Rabin Primality Test
    [0] Exit
""")
    
def main():
    status = True
    menu()
    while status:
        choose = input("Enter generator (1-5): ")
        if choose == "1":
            highest_prime, prime_count = findlargestPrime(60)
            print(f"Time ran: 60 seconds")
            print(f"Largest Prime(Trial Division): {highest_prime}")
            print(f"No of primes(Trial Division): {prime_count}")
        
        elif choose == "2":
            highest_prime, prime_count = optimizedfindlargestPrime(60)
            print(f"Time ran: 60 seconds")
            print(f"Largest Prime(Trial Division): {highest_prime}")
            print(f"No of primes(Trial Division): {prime_count}")
      
        elif choose == "3":
            highest_prime, prime_count = findLargestPrimeSOE(60)
            print(f"Time ran: 60 seconds")
            print(f"Largest Prime(Sieve of Eratosthenes): {highest_prime}")
            print(f"No of primes(Sieve of Eratosthenes): {prime_count}")
      
        elif choose == "4":
            highest_prime, prime_count = largestPrimeFermat(60)
            print(f"Time ran: 60 seconds")
            print(f"Largest Prime(Fermat Primality Test): {highest_prime}")
            print(f"No of primes(Fermat Primality Test): {prime_count}")
      
        elif choose == "5":
            highest_prime, prime_count = findLargestPrimeWF(60)
            print(f"Time ran: 60 seconds")
            print(f"Largest Prime(Wheel Factorization Method): {highest_prime}")
            print(f"No of primes(Wheel Factorization Method): {prime_count}")
      
        elif choose == "6":
            highest_prime, prime_count = findLargestPrimeMR(60)
            print(f"Time ran: 60 seconds")
            print(f"Largest Prime(Miller-Rabin Test): {highest_prime}")
            print(f"No of primes(Miller-RabinTest): {prime_count}")
        elif choose == "0":
            status = False
main()
