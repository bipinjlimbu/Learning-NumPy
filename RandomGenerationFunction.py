import numpy as np

# Normalized random numbers
normalized_random = np.random.rand(5) # 5 random numbers between 0 and 1 (size)
print("Normalized Random Numbers:")
print(normalized_random)

# Standarized random numbers
standardized_random = np.random.randn(5) # 5 random numbers from a standard normal distribution (size)
print("\nStandardized Random Numbers:")
print(standardized_random)

# Random integers
random_integers = np.random.randint(0, 10, 5) # 5 random integers between 0 and 9 (start, stop, size)
print("\nRandom Integers:")
print(random_integers)