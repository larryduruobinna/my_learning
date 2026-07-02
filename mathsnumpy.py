import numpy as np
# MATRIX:
matrix_grid = np.array([[4, 1, 0],
                        [2, 3, 1],
                        [0, 2, 5]])
print(matrix_grid.shape)

matrix_A = np.array([[4, 3, 9],
                     [1, 7, 3],
                     [0, 2, 6]])
print(matrix_A.shape)



# ADDITTION IN MATRIX:
# EXAMPLE1:
matrix_A = np.array([[4, 1],
                     [2, 3]])
matrix_B = np.array([[1, 0],
                     [0, 1]])
results_A = matrix_A + matrix_B
print(results_A)

#EXAMPLE2:
matrix_C = np.array([[6, 2],
                     [0, 5]])
matrix_D = np.array([[1, 3],
                     [4, 2]])
results_B = matrix_C + matrix_D
print(results_B)

# EXAMPLE3:
solar = np.array([[11, 20, 7],
                  [2, 17, 0],
                  [15, 4, 10]])
generator = np.array([[23, 42, 16],
                      [12, 19, 13],
                      [38, 22, 26]])
results = solar + generator
print(results)



# MULTIPLICATION IN MATRIX:
data_A = np.array([[2, 0],
                   [1, 3]])
data_B = np.array([[4, 1],
                   [2, 5]])
results_C = data_A @ data_B    # @ IS USED FOR MATRIX MULTIPLICATION NOT THE REGULAR *
print(results_C)



# IDENTITY MATRIX:

data_C = np.array([[3, 5],
                   [2, 7]])
data_I = np.eye(2)
results = data_C @ data_I
print(results)

data_D = np.array([[2, 7, 3],
                   [3, 9, 6],
                   [7, 1, 8]])
data_I = np.eye(3)
results = data_D @ data_I
print(results)

# INVERSE MATRIX:

data = np.array([[1, 2, 1],
                 [4, 4, 5],
                 [6, 7, 7]])
inv_data = np.linalg.inv(data)
print(inv_data)
check = data @ inv_data
print(check)
