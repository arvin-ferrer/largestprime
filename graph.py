import matplotlib.pyplot as plt
import numpy as np

# Data
methods = [
    "Trial Division",
    "Optimized Trial Division",
    "Sieve of Eratosthenes",
    "Fermat Primality Test",
    "Wheel Factorization",
    "Miller-Rabin Test"
]

# Largest primes found
largest_primes = [
    [117023, 119179, 113819],
    [4197833, 4393217, 4397311],
    [131071987, 131071987, 131071987],
    [11328931, 12075419, 11799919],
    [6754357, 6252401, 6792967],
    [10161923, 10244303, 9870811]
]

# Number of primes found
num_primes = [
    [11047, 11231, 10775],
    [296179, 308908, 309169],
    [7435597, 7435597, 7435597],
    [746850, 792751, 775835],
    [460988, 42897, 463416],
    [674672, 679713, 656636]
]

# Set up the figure
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Plotting Largest Primes
x = np.arange(len(methods))
width = 0.2

for i in range(3):
    ax1.bar(x + i * width, [largest_primes[j][i] for j in range(len(methods))], width, label=f'Attempt #{i + 1}')

ax1.set_xlabel('Prime Finding Methods')
ax1.set_ylabel('Largest Prime Found')
ax1.set_title('Largest Prime Found by Each Method')
ax1.set_xticks(x + width)
ax1.set_xticklabels(methods)
ax1.legend()
ax1.grid(axis='y')

# Plotting Number of Primes
for i in range(3):
    ax2.bar(x + i * width, [num_primes[j][i] for j in range(len(methods))], width, label=f'Attempt #{i + 1}')

ax2.set_xlabel('Prime Finding Methods')
ax2.set_ylabel('Number of Primes Found')
ax2.set_title('Number of Primes Found by Each Method')
ax2.set_xticks(x + width)
ax2.set_xticklabels(methods)
ax2.legend()
ax2.grid(axis='y')

# Show the plots
plt.tight_layout()
plt.show()
