import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Original Array:")
print(arr)

# Broadcasting 
print("\nBroadcasting Example:")
arr2 = np.array([[1], [2], [3], [4], [5]])
print("Array 1:")
print(arr)
print("Array 2:")
print(arr2)

result = arr + arr2
print("Result of Broadcasting (arr + arr2):")
print(result)