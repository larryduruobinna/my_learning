for reading in range(4):
    print(f"Reading number {reading}")
for i in range(5):
    voltage = i * 100
    print(voltage)
#USING F STRING INSIDE LOOPS
for i in range(5):
    voltage = i * 100
    print(f"Reading {i}: Voltage is {voltage}V")
for i in range(10):
    current = i * 10
    print(f"Reading {i}: Current is {current}A")

# LOOPS THROUGH A LIST:
voltages = [220, 230, 240, 250, 260]
for v in voltages:
    print(f"Voltage readings: {v}V")

voltages = [220, 230, 240, 250,260]
for v in voltages:
    if v > 240:
        print(f"{v}V - HIGH VOLTAGE!")
    else:
        print(f"{v}V - Safe")
current = [15, 20, 5, 9, 12]
for c in current:
    if c > 9:
        print(f"{c}A - HIGH CURRENT!")
    else:
        print(f"{c}A - NORMAL SAFE!")

# COUNTING INSIDE A LOOP:
voltages = [220, 230, 240, 250, 260]
danger_count = 0
safe_count = 0

for v in voltages:
    if v > 240:
        danger_count = danger_count + 1   
    else:
        safe_count = safe_count + 1
print(f"Total dangerous readings: {danger_count}")
print(f" Total Safe readings: {safe_count}")

# SUMMING IN A LOOP:

power_readings = [100, 150, 200, 175, 120]
total_power = 0

for p in power_readings:
    total_power = total_power + p
print(f"Total power reading: {total_power}W")

voltage_readings = [220, 230, 240, 250, 260]
total = sum(voltage_readings)
count = len(voltage_readings)
average = total/count
total_high_voltage = 0
total_normal_voltage = 0
max_voltage = voltage_readings[0]
for v in voltage_readings:
    if v > max_voltage:
        max_voltage = v
for v in voltage_readings:
    if v > 240:
        total_high_voltage = total_high_voltage + v
    else:
        total_normal_voltage = total_normal_voltage + v
print(f"Max voltage: {max_voltage}V")
print(f"Total high voltage: {total_high_voltage}V")
print(f"Total safe voltage: {total_normal_voltage}V")
print(f"Average voltages: {average}V")

max_voltage = max(voltage_readings)
print("Max voltage:", max_voltage,"V")
