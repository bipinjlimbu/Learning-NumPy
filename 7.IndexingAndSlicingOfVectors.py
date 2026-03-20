import numpy as np

arr = np.arange(1, 11)
print("Original Array:")
print(arr)

# Indexing
print("\nElement at index 0:", arr[0]) # indexing starts at 0
print("Element at index 4:", arr[4])

# Slicing
print("\nSliced Array (index 2 to 5):")
print(arr[2:6]) # slicing is exclusive of the stop index
print("\nSliced Array (every other element):")
print(arr[::2]) # slicing every other element