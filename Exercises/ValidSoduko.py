import numpy as np

s = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])

for i in range(0,9,3):
    for j in range(0,9,3):
        block = s[i:i+3, j:j+3]
        if np.sum(block) != 45:
            print("The Sudoku is not valid.")
            exit()

row_sums = np.sum(s, axis=1)
col_sums = np.sum(s, axis=0)

if np.all(row_sums == 45) and np.all(col_sums == 45):
    print("The Sudoku is valid.")
else:
    print("The Sudoku is not valid.")