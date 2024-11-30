#!/usr/bin/env python3

""" Chapter 5. Case Study: Hacker Statistics

    -- Random number generator
"""

import numpy as np
import time

# Create a random number generator instance (this is the recommended way)
rng = np.random.default_rng(seed=123)

# Generate a random float between 0 and 1
random_float = rng.random()
print(f"Random float: {random_float}")

# Generate random integers between 1 and 10
random_int = rng.integers(low=1, high=11)
print(f"Random integer: {random_int}")

# Generate an array of random numbers
random_array = rng.random(size=5)
print(f"Random array: {random_array}")

# Generate random numbers from a normal distribution
normal_dist = rng.normal(loc=0, scale=1, size=5)
print(f"Normal distribution samples: {normal_dist}")

"""
Note: Using np.random.default_rng() is the modern and recommended way to generate
random numbers in NumPy. It provides better statistical properties and is more
future-proof than the older np.random.seed() approach.

Key benefits:
1. Better random number generation algorithms
2. Thread-safe operations
3. More explicit state management
4. Better performance
"""

"""
When to use fixed seed (e.g., seed=123):
1. During development and testing
2. When you need reproducible results
3. For scientific experiments that need to be replicated
4. For debugging purposes

When to use time-based seed:
1. In production when you want truly random numbers
2. For games or simulations where unpredictability is desired
3. For security-related applications
4. When you don't need to reproduce the results
"""

# Example 1: Using current time as seed
time_seed = int(time.time() * 1000)  # Convert to milliseconds
rng_time = np.random.default_rng(seed=time_seed)
print(f"Random number with time seed: {rng_time.random()}")

# Example 2: Using fixed seed for reproducibility
rng_fixed = np.random.default_rng(seed=123)
print(f"Random number with fixed seed: {rng_fixed.random()}")

# Example 3: Using no seed (NumPy will automatically use a random seed)
rng_auto = np.random.default_rng()
print(f"Random number with auto seed: {rng_auto.random()}")