import numpy as np

arr = np.arange(1, 31).reshape(5, 6)
print("Original Array:")
print(arr)

# Indexing
print("\nElement at row 2, column 3:", arr[1, 2]) # indexing starts at 0
print("Element at row 4, column 5:", arr[3, 4])

# Slicing
print("\nSliced Array (rows 1 to 3, columns 2 to 4):")
print(arr[0:3, 1:4]) # slicing is exclusive of the stop index
print("\nSliced Array (all rows, columns 3 to 5):")
print(arr[:, 2:5]) # slicing all rows, columns 2 to 4
print("\nSliced Array (rows 2 to 5, all columns):")
print(arr[1:5, :]) # slicing rows 1 to 4, all columns
print("\nSliced Array (every other row and column):")
print(arr[::2, ::2]) # slicing every other row and column

