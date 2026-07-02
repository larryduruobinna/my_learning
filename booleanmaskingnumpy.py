import numpy as np
# BOOLEAN MASKING MEANS FILTERING AN ARRAY BASED ON CONDITIONS. 
# STEP 1: CREATING THE MASK,
voltages = np.array([220, 245, 235, 250, 215, 238])
mask = voltages > 240
print(mask)
# STEP2: USING THE MASK TO FILTER,
fault = voltages[voltages > 240]
print("Voltage faults:", fault)

# COMBINING CONDITIONS: readings between 220 and 240
normal_voltage = voltages[(voltages >= 220) & (voltages <= 240)]
print("Normal voltage readings:", normal_voltage)


# CHALLENGE:
currents = np.array([12, 18, 45, 22, 8, 50, 19, 33, 15, 60])
faults = currents[currents > 30]
print("Readings above 30:", faults)
print("Readings above 30:", currents[currents > 30])
#readings between 10 and 25:
normal_currents = currents[(currents >= 10) & (currents <= 25)]
print(normal_currents)
print("Readings count above 30:", len(faults))

# CHALLENGE 2:
grid = np.array([[225, 230, 228, 235, 240, 238, 222, 219, 233, 227, 231, 226],
                 [210, 215, 212, 208, 214, 211, 209, 213, 216, 210, 212, 211],
                 [240, 238, 242, 239, 241, 243, 237, 240, 244, 239, 241, 240],
                 [195, 200, 198, 350, 202, 199, 196, 201, 197, 200, 198, 199],
                 [220, 215, 218, 212, 216, 219, 214, 217, 221, 215, 218, 220]])

over_voltage = grid[grid > 245]
under_voltage = grid[grid < 200]
normal_voltage = grid[(grid >= 200) & (grid <= 245)]
normal_voltage_sum = np.sum(normal_voltage)
total_voltage = np.sum(grid)
ratio_normal_voltage = normal_voltage_sum / total_voltage
total_fault_voltages = len(over_voltage) + len(under_voltage)
print("Over voltage readings:", over_voltage)
print("Over voltage readings count:", len(over_voltage))
print("Over voltage substations:", grid[3])
print("Under voltage readings:", under_voltage)
print("Under voltage readings count:", len(under_voltage))
print("Under voltage readings substation:", grid[3])
print("Normal voltage counts:", len(normal_voltage))
print("percentage of normal readings to total readings:", ratio_normal_voltage * 100)
print("Fault voltages:", (under_voltage) | (over_voltage))
print("Total fault voltages counts:", total_fault_voltages)