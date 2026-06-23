import numpy as np
# HOW TO CREATE A 2D ARRAY:

grid = np.array([[220, 225, 230, 228], [210, 215, 212, 218], [240, 238, 235, 242]])
print("Shape:", grid.shape)

# HOW TO ACCESS VALUES IN A 2D ARRAY:
print(grid[0,2])
print(grid[1,3])

# HOW TO ACCESS A FULL ROW:
print(grid[0])
print(grid[2])

# HOW TO ACCESS A FULL COLUMN:
print(grid[:,0])
print(grid[:,3])

# MATH ON 2D ARRAY:
#ADD 5 TO EVERY VALUE:
print(grid + 5)

# STATISTICAL FUNCTIONS WORK TOO:
print("Max grid:", np.max(grid))
print("Min grid:", np.min(grid))
print("Total grid:", np.sum(grid))
print("Average grid:", np.mean(grid))

# STATS PER ROW
print("Max grig per line:", np.max(grid, axis=1))
print("Min per line:", np.min(grid, axis=1))

# STATS PER COLUMN:
print("Max per hour:", np.max(grid, axis=0))
print("Average per hour:", np.mean(grid, axis=0))


# CHALLENGE
transformer = np.array([[225, 230, 228, 235, 229], [210, 215, 212, 208, 214], [240, 238, 242, 239, 241]])
print("Transformer shape:",transformer.shape)
print("tr2-readind3:",transformer[1, 2])
print("TR3:",transformer[2])
print("Hour1:",transformer[:, 0])
print("Max voltage:", np.max(transformer))
print("Average voltage TR1:", np.mean(transformer, axis=1))



grid = np.array([[12, 15, 18, 20, 17, 14], [8, 10, 12, 15, 13, 11], [20, 22, 25, 28, 24, 21], [5, 7, 9, 11, 8, 6]])
print("Grid shape:", grid.shape)
print("Current at feeder3 hr4:", grid[2, 3])
print("Feeder1:", grid[0])
print("Feeder hr3:", grid[:, 2])
print("Fault currents:", grid * 1.2)
print("Max current per feeder:", np.max(grid, axis=1))
print("Average current per hour:", np.mean(grid, axis=0))
print("Reshape:", grid.reshape(6, 4))