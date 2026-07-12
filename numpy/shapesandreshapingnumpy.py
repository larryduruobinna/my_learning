#  WHAT IS A SHAPE?    SHAPE MEANS HOW MANY ROWS AND COLUMNS AN ARRAY HAS.

import numpy as np
voltages = np.array([220, 215, 230, 210, 225])
print(voltages.shape)

# RESHAPING: THIS MEANS CHANGING HOW THE DATA IS ARRANGED WIHTOUT CHANGING THE VALUES.   SAME READINGS DIFFERENT ARRANGEMENTS

readings = np.array([2, 5, 1, 4, 3, 9, 12, 7, 8, 6])
reshaped = readings.reshape(2,5)
print(reshaped)

currents = np.array([2, 8, 12, 15, 7, 18])
reshaped = currents.reshape(2, 3)
print(reshaped)

# SUBSTATIONS
voltage_readings = np.array([220, 221, 219, 222, 230, 231, 229, 228, 210, 211, 209, 212])
substation = voltage_readings.reshape(3, 4)
print(substation)


# CHALLENGE
currents = np.array([5, 10, 15, 20, 25, 30, 35, 40])
reshaped1 = currents.reshape(2, 4)
reshaped2 = currents.reshape(4, 2)

print(currents.shape)
print(reshaped1)
print(reshaped2)


