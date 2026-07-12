import numpy as np
# ARRAYS: An array is like a python list. But made for numbers and math.
# pythonlist
voltages = [230, 240, 250]
# NumPy array
voltages = np.array([230, 240, 250])

#why use arrays?   with a python list, math needs a loop:
for v in voltages:
    print(v * 2)
# with numpy array, one line does everything:
print(voltages * 2)

# ARRAY OPERATIONS:
# WHAT IS AN ARRAY OPERATION?  IT MEANS DOING MATH ON EVERY VALUE IN THE ARRRAY AT ONCE.  NO LOOP NEEDED. ONE LINE DOES EVERYTHING.

#NORMAL PYHTON WAY: EXAMPLES 
voltage = [220, 230, 240]
for v in voltage:
    print(v + 10)

# NUMPY WAY:
voltage = np.array([220, 230, 240])
print(voltage + 10)


voltage = np.array([240, 250, 260, 270])
current = np.array([15, 25, 30, 32])
power = voltage * current
print(power)


voltage = np.array([220, 230, 240, 210])
current = np.array([5, 6, 4, 7])
power = voltage * current 
print(power)

# ALL BASIC MATH WORKS THE SAME WAY
voltage = np.array([220, 230, 240])
print(voltage + 10)
print(voltage - 10)
print(voltage * 2)
print(voltage / 2)


# CHALLENGE:

currents = np.array([2, 4, 6, 8, 10])
resistor = 5
voltage = currents * resistor
print(voltage)

# CHALLENGE 2:
voltages = np.array([220, 215, 230, 210, 225])
currents = np.array([10, 12, 8, 15, 11])
resistance = 0.5
power = voltages * currents
voltage_drop = currents * resistance
actual_voltage = voltages - voltage_drop
print(power)
print(voltage_drop)
print(actual_voltage)