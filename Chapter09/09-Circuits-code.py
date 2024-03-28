import math
import matplotlib.pyplot as plt
import numpy as np

# Invert a vector of floats around the mean of
# the elements

def invert_about_mean(vector: list[float]) -> list[float]:
    mean = float(sum(vector)) / len(vector)
    return [2 * mean - s for s in vector]

# Compute the maximum obtained amplitude and iteration
# number when it is obtained via amplitude amplification

def compute_maximum_amplitude(N: int) -> tuple[int]:
    vector = [1.0 / math.sqrt(N)] * N
    max_amplitude = 0.0
    max_amplitude_iteration = 0
    iteration = 1

    while True:
        # Negate the first amplitude
        vector[0] = -vector[0]

        # Invert about the mean
        vector = invert_about_mean(vector)

        if vector[0] > max_amplitude:
            max_amplitude = vector[0]
            max_amplitude_iteration = iteration
            iteration += 1
        else:
            return max_amplitude, max_amplitude_iteration

compute_maximum_amplitude(2**10)

