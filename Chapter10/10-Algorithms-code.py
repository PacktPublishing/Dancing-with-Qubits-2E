def list_of_primes(n):
    # Return a list of primes <= n using the
    # Sieve of Eratosthenes

    # Prepare the list of numbers containing [0,1,...,n]
    numbers = list(range(n + 1))

    # Mark the first two numbers by setting them to 0
    numbers[0] = numbers[1] = 0

    # The first prime is 2
    p = 2

    # Cycle through the numbers, marking nonprimes
    while p < n:
        if p:
            index = p + p
            while index <= n:
                numbers[index] = 0
                index += p
        p += 1

    # Return the primes left in the list
    return [i for i in numbers if i != 0]

import random
random.seed(1.5)
[random.randint(5, 17) for _ in range(10)]

[3**n for n in range(12)]

[3**n % 13 for n in range(12)]

[3**n % 16 for n in range(12)]

[3**n % 22 for n in range(12)]

