import math
math.log(10**-6) / math.log(0.6)

import random

def sample_n_times(probabilities, n):
    # set seed for repeatability
    random.seed(n)

    probability_sums = []
    number_of_probabilities = len(probabilities)
    sum = 0.0
    for probability in probabilities:
        sum += probability
        probability_sums.append(sum)

    # ensure final value is 1.0 to avoid round-off error
    probability_sums[number_of_probabilities - 1] = 1.0
    counts = [0 for probabilities in probabilities]

    for _ in range(n):
        r = random.random()
        for j in range(number_of_probabilities):
            if r < probability_sums[j]:
                counts[j] = counts[j] + 1
                break

    pad_width = len(str(len(probabilities)))
    print(f"\nResults for {n} simulated samples")
    print("\nEvent  Actual Probability  Simulated Probability")
    for j in range(number_of_probabilities):
        print(f"  {j:{pad_width}}{(13-pad_width)*' '}"
              f"{probabilities[j]}{14*' '}"
              f"{round(float(counts[j])/n, 4)}")

sample_n_times([0.15, 0.37, 0.26, 0.22], 100)

sample_n_times([0.15, 0.37, 0.26, 0.22], 1000000)

from math import pi
x = (pi**2 / 16.0 - pi / 4.0 + 0.5) / (1/400)**2
print(f"{x:,.3f}")    # print x to 3 decimal places with commas

print(f"{(x/0.0001):,.3f}")

print(f"{(x/0.00001):,.3f}")

