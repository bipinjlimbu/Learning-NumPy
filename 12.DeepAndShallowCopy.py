import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Original Array:")
print(arr)

# Deep Copy
deep_copy_arr = arr.copy()
deep_copy_arr[0] = 10
print("\nDeep Copy Array (after modification):")
print(deep_copy_arr)
print("Original Array (after deep copy modification):")
print(arr)

# Shallow Copy
shallow_copy_arr = arr
shallow_copy_arr[0] = 20
print("\nShallow Copy Array (after modification):")
print(shallow_copy_arr)
print("Original Array (after shallow copy modification):")
print(arr)