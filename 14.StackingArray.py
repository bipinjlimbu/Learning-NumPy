import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Vertical Stacking
vertical_stack = np.vstack((a, b))
print("Vertical Stack:")
print(vertical_stack)

# Horizontal Stacking
horizontal_stack = np.hstack((a, b))
print("\nHorizontal Stack:")
print(horizontal_stack)

# Column Stacking
column_stack = np.column_stack((a, b))
print("\nColumn Stack:")
print(column_stack)