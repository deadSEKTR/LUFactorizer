import numpy as np

def gauss_transformation(matrix):
    n = len(matrix)
    gauss_matrix = np.identity(n)

    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][i] == 0:
                return None  # Gauss elimination cannot proceed if diagonal element is zero
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(n):
                matrix[j][k] -= ratio * matrix[i][k]
                gauss_matrix[j][k] -= ratio * gauss_matrix[i][k]
    
    return gauss_matrix

# Input matrix here:
matrix = [[1, 2, 1],
          [3, 8, 1],
          [0, 4, 1]]

gauss_matrix = gauss_transformation(matrix)
if gauss_matrix is not None:
    print("Gauss Transformation Matrix:")
    print(gauss_matrix)
else:
    print("Gauss elimination cannot be applied because a diagonal element is zero.")
