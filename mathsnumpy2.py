import numpy as np

data_A = np.array([[2, 8],
                   [4, 1]])
data_B = np.array([[3, 6],
                   [0, 5]])
results = data_A @ data_B
print(results)


data_C = np.array([[4, 7],
                   [3, 1]])
data_I = np.eye(2)
results = data_C @ data_I
print(results)



data_D = np.array([[4, 9, 1],
                   [3, 2, 0],
                   [7, 4, 8]])
inv_D = np.linalg.inv(data_D)
print(inv_D)
check = data_D @ inv_D
print(check)