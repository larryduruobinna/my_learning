import numpy as np
readings = np.array([225, 230, 228, 235, 240, 238, 220, 215, 222, 218, 230, 225])
fault_boost = readings + 5
turns_ratio = 2
output_voltages = readings/turns_ratio
substation = readings.reshape(3, 4)
print("Shape:", readings.shape)
print("First_readings:", readings[0])
print("Last_readings:", readings[-1])
print("Peak_hours:", readings[4:8])
print("Fault_boost:", fault_boost)
print("Output_voltages:", output_voltages)
print("Reshape:", substation)


readings = np.array([225, 230, 228, 235, 210, 215, 212, 218, 240, 238, 242, 236])
reshaped = readings.reshape(3, 4)
voltage_surge = readings + 8
stepdown = readings/2
print("Shape:", readings.shape)
print("Reshape:", reshaped)
print("First_reading:", readings[0])
print("Last_reading", readings[-1])
print("Voltage_surge:", voltage_surge)
print("stepdown:", stepdown)



currents = np.array([5, 8, 12, 20, 35, 40, 38, 30, 25, 20])
resistance = 2
voltage = currents * resistance
reshaped = currents.reshape(2, 5)
print("Shape:", currents.shape)
print("Startup surge:", currents[5])
print("First 3 readings:", currents[:3])
print("Last 4 readings:", currents[6:])
print("Voltages:", voltage)
print("Reshape:", reshaped)



#POWER GRID FAULT ANALYSIS

voltages = np.array([225, 230, 228, 235, 240, 238, 220, 215, 222, 218, 230, 225, 219, 221, 233])
fault_period = voltages[4:9]
after_lightning_strike = voltages + 15
turns_ratio = 11
transformer_output = voltages/turns_ratio
print("Shape:", voltages.shape)
print("Grid shifts:", voltages.reshape(3, 5))
print("Fault periods", fault_period)
print("After lightning strike:", after_lightning_strike)
print("Transformer output:", transformer_output)
print("First reading:", voltages[0])
print("Last reading:", voltages[-1])


# SUBSTATION CABLE ANALYSIS
cable1 = np.array([10, 12, 15, 18, 20, 22])
cable2 = np.array([8, 9, 11, 14, 16, 18])
cable3 = np.array([5, 7, 9, 12, 14, 16])
resistance = 0.8
voltage1 = cable1 * 0.8
voltage2 = cable2 * 0.8
voltage3 = cable3 * 0.8
total_current = cable1 + cable2 + cable3
cable1_fault = cable1 * 1.3
print("Shape of cable1:", cable1.shape)
print("Voltage drop1:", voltage1)
print("Voltage drop2:", voltage2)
print("Voltage drop3:", voltage3)
print("Total current:",total_current)
print("Cable1 after fault:", cable1_fault)
print("Cable1 reshaped:", cable1.reshape(2, 3))
print("Cable3 last 3:", cable3[3:])