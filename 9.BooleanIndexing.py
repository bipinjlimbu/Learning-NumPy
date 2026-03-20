import numpy as np

arr = np.arange(11, 21)
print("Original Array:")
print(arr)

# Boolean Indexing
# Create a boolean array where the condition is True for elements that are even
bool_arr = arr % 2 == 0
print("\nBoolean Array (True for even numbers):")
print(bool_arr)

# Use the boolean array to index the original array
print("\nElements that are even:")
print(arr[bool_arr])