import numpy as np
#STATISTICAL FUNCTIONS: Statistical functions analyze for data automatically. Instead of writing code to find the highest voltage manually-numpy does it in one line.
# EXAMPLE:
readings = np.array([220, 215, 230, 210, 225])

print("Max:", np.max(readings))
print("Min:", np.min(readings))
print("Mean:", np.mean(readings))
print("Sum:", np.sum(readings))

# one more useful function is the standard deviation(std), it tells you how much your readings are jumping around.
# low std = stable readings. good.
# high std = unstable readings. possible fault. these are very useful in power monitoring.
print("std:", np.std(readings))


#Example:

power = np.array([150, 180, 200, 175, 190, 160])

print("Max power:", np.max(power))
print("Min power:", np.min(power))
print("Average power:", np.mean(power))
print("Total power:", np.sum(power))
print("Stability:", np.std(power))


# CHALLENGE:

currents = np.array([15, 18, 22, 30, 25, 20, 17, 28])

print("Max current:", np.max(currents))
print("Min current:", np.min(currents))
print("Average current:", np.mean(currents))
print("Total current:", np.sum(currents))
print("Stability:", np.std(currents))