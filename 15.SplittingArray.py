import numpy as np

a = np.arange(1,9).reshape(2,4)
print("Original Array:")
print(a)

# Horizontal Split
h_split = np.hsplit(a, 2)
print("\nHorizontal Split:")
print(h_split)

# Vertical Split
v_split = np.vsplit(a, 1)
print("\nVertical Split:")
print(v_split)