import numpy as np

# Matrix Creation
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

# Matrix Addition
matrix_sum = matrix_a + matrix_b
print("\nMatrix A + Matrix B:")
print(matrix_sum)

# Matrix Subtraction
matrix_diff = matrix_a - matrix_b
print("\nMatrix A - Matrix B:")
print(matrix_diff)

# Matrix Multiplication
matrix_product = np.dot(matrix_a, matrix_b)
print("\nMatrix A * Matrix B:")
print(matrix_product)

# Element-wise Multiplication
elementwise_product = matrix_a * matrix_b
print("\nElement-wise Multiplication of Matrix A and Matrix B:")
print(elementwise_product)

# Transpose of a Matrix
transpose_a = np.transpose(matrix_a)
print("\nTranspose of Matrix A:")
print(transpose_a)

# Inverse of a Matrix
inverse_a = np.linalg.inv(matrix_a)
print("\nInverse of Matrix A:")
print(inverse_a)

# Determinant of a Matrix
det_a = np.linalg.det(matrix_a)
print("\nDeterminant of Matrix A:")
print(det_a)

# Eigenvalues and Eigenvectors
eigenvalues_a, eigenvectors_a = np.linalg.eig(matrix_a)
print("\nEigenvalues of Matrix A:")
print(eigenvalues_a)
print("\nEigenvectors of Matrix A:")
print(eigenvectors_a)