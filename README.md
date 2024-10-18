# Generating Prime Numbers Using Various Algorithms

## Table of Contents

- [I. Introduction](#Introduction)
- [II. Installation](#Installation)
- [III. Usage](#Usage) 
- [IV. Algorithms Implemented](#Algorithms-implemented)
  - [1. Basic Trial Division](#Basic-trial-division)
  - [2. Sieve of Eratosthenes](#Sieve-of-eratosthenes)
  - [3. Miller-Rabin Primality Test](#Miller-rabin-primality-test)
  - [4. Fermat Primality Test](#4-fermat-primality-test)
- [V. Performance and Time Complexity](#v-performance-and-time-complexity)
  - [1. Basic Trial Division](#1-basic-trial-division-1)
  - [2. Optimized Division](#2-optimized-division)  
  - [3. Sieve of Eratosthenes](#3-sieve-of-eratosthenes)
  - [4. Miller-Rabin Primality Test](#4-miller-rabin-primality-test)
  - [5. Fermat Primality Test](#5-fermat-primality-test)
- [VI. Conclusion](#vi-conclusion)
- [VII. License](#vii-license)


## Introduction
In my third-week exercise, my professor added a bonus task in which we had to generate prime numbers up to the nth integer. I didn't finish it because, well, skill issue. So, I decided to take my time and create this small project during my reading break instead of actually reviewing for my midterm exams. So, what are prime numbers?

According to a website I read, a prime number is a natural number that is divisible by 1 and itself. Some of the prime numbers include 2, 3, 5, 7, 11, 13, etc. Prime numbers play a crucial role in various fields, particularly in cybersecurity, cryptography, number theory, and algorithm design. Efficient prime number generation is essential for many computational tasks. This so-called "academic blog" presents multiple algorithms for generating prime numbers and analyzes their computational complexity. The objective is to explore the different methods for generating prime numbers, identify which algorithm is the most efficient for generating large prime numbers, and highlight the trade-offs in terms of speed, accuracy, and scalability.

## Installation
Just clone this repository.
```bash
git clone https://github.com/arvin-ferrer/largestprime.git
```
For data visualization you need to have matplotlib and numpy. I provided some sample data and graph for you to follow
```
pip install matplotlib
pip install numpy
```
or 
```
pip install -r requirements.txt
```

## Usage
For data visualization you need to have matplotlib and numpy. I provided some sample data and graph for you to follow.
```
python3 graph.py
```
To use the actual program 
```
python3 main.py
```
## Algorithms Implemented
### Basic Trial Division
The **Trial Division** algorithm is the simplest approach to determine whether a number is prime. It works by testing divisibility of a number \(n\) by every integer from 2 to $(\sqrt{n})$. If $\(n\)$ is divisible by any of these integers, it is composite; otherwise, it is prime.

Theorem: Let $a$ and $n$ be integers such that $a<n≤a2a<n≤a2$. The integer n is prime if and only if $gcd⁡(n,a!)=1gcd(n,a!)=1.$

When searching for a large prime number (such as a titanic prime), it is impractical to divide by all primes below the square root. Nonetheless, we still utilize trial division for initial screening: when determining if $n$ is prime, we first divide $n$ by several million small primes before applying a more rigorous primality test.


```
PSEUDOCODE FOR THE BASIC TRIAL DIVISION IT CHECKS THE DIVISIBILITY OF ALL NUMBERS UP TO N-1.
function trialDivision(n):
    if n is less than 2:
        return False
    for i from 2 to n-1:
        if n modulo i is 0:
            return False
    return True

function findLargestPrime(limit):
    start timer
    count = 0
    largest_prime = 2
    num = 2
    while time elapsed is less than limit:
        if trialDivision(num) is True:
            largest_prime = num
            count = count + 1
        num = num + 1
    return largest_prime, count

PSEUDOCODE FOR THE OPTIMIZED VERSION SAME CONCEPT HOWEVER IT ONLY CHECK THE DIVISIBILITY
OF ALL NUMBERS UP TO SQUARE ROOT OF N.
function optimizedTrialDivision(n):
    if n is less than 2:
        return False
    for i from 2 to square root of n:
        if n modulo i is 0:
            return False
    return True

function optimizedFindLargestPrime(limit):
    start timer
    largest_prime = 2
    count = 0
    num = 2
    while time elapsed is less than limit:
        if optimizedTrialDivision(num) is True:
            largest_prime = num
            count = count + 1
        num = num + 1
    return largest_prime, count

```
### Sieve of Eratosthenes
The **Sieve of Eratosthenes** is an efficient algorithm for generating all prime numbers up to a specified limit. It starts by listing all the numbers from 1 to n (or from 2 to n, since 1 is neither prime nor composite). It then marks all the multiples of the first prime number, which is 2. After marking off the multiples of 2, it proceeds to mark all the multiples of the next prime number, which is 3. This process continues until there are no remaining primes less than n. In the end, the unmarked numbers represent all the prime numbers less than n.

Theorem 2: "If we have marked off all the multiples of all the prime numbers up to and including p, then the least multiple of the next prime number $p + x$ (where x is even) that is unmarked is $(p + x)^2$". 
(Too lazy to rephrase this shit.)
```
SieveOfEratosthenes(n)
    Input:
        n - the upper limit (inclusive) to find prime numbers
    Output:
        A list of prime numbers up to n

    1. Create a boolean array isPrime[0...n], and initialize each value to true
    2. Set isPrime[0] and isPrime[1] to false (0 and 1 are not prime)
    
    3. For p = 2 to sqrt(n):
        a. If isPrime[p] is true:
            i.  Mark all multiples of p as false:
                For i = p*p to n step p:
                    Set isPrime[i] = false
    
    4. Collect all indices where isPrime[i] is true and return them as the list of primes

```
### Miller-Rabin Primality Test
The Rabin-Miller test improves upon Fermat's Test by addressing Carmichael numbers. This method is a probabilistic method, but it is generally preferred over Fermat’s method.
```
bool isPrime(int n, int k)
// This function checks if 'n' is prime. It returns false if 'n' is composite 
// and true if 'n' is likely to be prime. The parameter 'k' controls the level 
// of accuracy, with a higher 'k' providing more reliable results.

1) Handle base cases where n < 3.
2) If 'n' is even, return false (since all even numbers greater than 2 are composite).
3) Find an odd number 'd' such that (n-1) can be written as d * 2^r, where r > 0 
   (since n-1 is even, r is greater than 0).
4) Repeat the following 'k' times:
     if (millerTest(n, d) == false)
          return false  // n is composite
5) Return true, meaning 'n' is probably prime.

// The millerTest function is executed for 'k' trials. It returns false if 'n' 
// is composite and true if 'n' is probably prime.
// 'd' is the odd number such that d * 2^r = n - 1 for some r >= 1.
bool millerTest(int n, int d)
1) Select a random number 'a' from the range [2, n-2].
2) Compute x = a^d % n.
3) If x is 1 or n-1, return true, as n may be prime.

// The following loop runs 'r-1' times:
4) Repeat until 'd' reaches n-1:
     a) Set x = (x * x) % n.
     b) If x becomes 1, return false, indicating that 'n' is composite.
     c) If x becomes n-1, return true, indicating that 'n' is probably prime.

why the f am I doing this shit :> 

```
### Fermat Primality Test
This is similar to Rabin-Miller Test. This method is also a probabilistic method.
Fermat's theorem says that if $p$ is prime and $a$ is not divisible by $p$, then 
$a^(p-1) = 1 (mod p)$.
To test whether a number $p$ is prime, we can choose random integers a that are not divisible by $p$, and check if a specific congruence condition is satisfied. If the condition fails for any value of a, then p is composite. On the other hand, if p is composite, it's highly unlikely that the congruence will hold for a randomly chosen a. Therefore, if the congruence holds for one or more values of $a$, we can conclude that pp is likely prime, though not guaranteed.

```
FermatPrimalityTest(n, k)
    Input: 
        n - the number to be tested for primality
        k - the number of iterations to perform (higher k means more accuracy)
    Output: 
        true - if n is probably prime
        false - if n is composite

    1. If n <= 1, return false
    2. If n == 2, return true (2 is prime)
    3. If n is even, return false (all even numbers other than 2 are composite)

    4. Repeat k times:
        a. Pick a random integer 'a' such that 2 <= a <= n-2
        b. Compute: result = a^(n-1) mod n
        c. If result != 1, return false (n is composite)

    5. If the loop completes without returning false, return true (n is probably prime)

```
## Performance Comparison
| Algorithm                  | Time Complexity        | Space Complexity | Accuracy          |
|----------------------------|------------------------|------------------|-------------------|
| **Basic Trial Division**    | `O(n)`                 | `O(1)`           | 100%              |
| **Optimized Trial Division**| `O(√n)`                | `O(1)`           | 100%              |
| **Sieve of Eratosthenes**   | `O(n log log n)`       | `O(n)`           | 100%              |
| **Miller-Rabin Test**       | `O(k log^3 n)`         | `O(log n)`       | Probabilistic, very accurate with high `k` |
| **Fermat Test**             | `O(k log^3 n)`         | `O(log n)`       | Probabilistic, lower accuracy compared to Miller-Rabin |
## Conclusion
This so called "academic blog" presents and compares the different algorithm that I used for generating prime numbers. For small-scale applications, **Basic Trial Division** and **Sieve of Eratosthenes** offer reliable and efficient solutions. For large numbers or cryptographic use cases, Miller-Rabin and Fermat tests provide faster alternatives with high probability of correctness. The choice of algorithm depends on the specific requirements of speed, accuracy, and scale. 

PS: If you want a fast algorithm for generating prime numbers up to nth number just use Sieve of Eratosthenes(damn so mouthful) or its relative called **Sieve of Atkin**(I didn't know about this until I'm 80% done f my life). Also If you're wondering why I did this in python and not C or C++ that's because I'm too  dumb to implement the Fermat's theorem and Miller-Rabin Test in low-level languages.


## Resources that I used
```
too lazy to cite this properly sorry

https://byjus.com/maths/prime-numbers/
https://t5k.org/glossary/page.php?sort=TrialDivision
https://www.geeksforgeeks.org/trial-division-algorithm-for-prime-factorization/
https://en.wikipedia.org/wiki/Miller%E2%80%93Rabinprimalitytest
https://www.geeksforgeeks.org/fermat-method-of-primality-test/
https://en.wikipedia.org/wiki/ProofsofFermat'slittletheorem

```
## License

[MIT](https://choosealicense.com/licenses/mit/)
