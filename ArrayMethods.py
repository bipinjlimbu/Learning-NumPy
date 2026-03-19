import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Array:")
print(arr)

# Methods
print("\nSum:", arr.sum(1)) # sum of all elements in the array (axis can be specified for sum along a specific axis)
print("Mean:", arr.mean(1)) # mean of all elements in the array (axis can be specified for mean along a specific axis)
print("Max:", arr.max(1)) # maximum value in the array (axis can be specified for max along a specific axis)
print("Min:", arr.min(1)) # minimum value in the array (axis can be specified for min along a specific axis)
print("Standard Deviation:", arr.std(1)) # standard deviation of the elements in the array (axis can be specified for std along a specific axis)
print("Cumulative Sum:", arr.cumsum(1)) # cumulative sum of the elements in the array (axis can be specified for cumsum along a specific axis)
print("Cumulative Product:", arr.cumprod()) # cumulative product of the elements in the array
print("Unique Elements:", np.unique(arr)) # unique elements in the array
print("Sorted Array:", np.sort(arr)) # sorted array
print("Transpose:", arr.T) # transpose of the array
print("Argmax:", arr.argmax()) # index of the maximum value in the array
print("Argmin:", arr.argmin()) # index of the minimum value in the array