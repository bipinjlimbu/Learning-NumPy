import numpy as np

arr = np.arange(1, 22)
print("Original Array:")
print(arr)

# Reshape the array to 3 rows and 7 columns
reshaped_arr = arr.reshape(3, 7)
print("\nReshaped Array (3x7):")
print(reshaped_arr)

# Resize the array to 4 rows and 6 columns (note: this will change the original array)
arr.resize(4, 6)
print("\nResized Array (4x6):")
print(arr)

#Resize vs Reshape
# Reshape does not change the original array, it returns a new array with the specified shape
# Resize changes the original array and can also change the total number of elements in the array
# If the new shape has more elements than the original array, the new elements will be filled with zeros
# If the new shape has fewer elements than the original array, the extra elements will be discarded