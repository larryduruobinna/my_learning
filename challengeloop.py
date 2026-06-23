# CHALLENGE: SOLAR PANEL DAILY OUTPUT ANALYZER.
power_readings = [120, 250, 480, 650, 720, 680, 450, 220]
total_energy = sum(power_readings)
count = len(power_readings)
average_power_output = total_energy/count
max_power = max(power_readings)
lowest_power = min(power_readings)
no_high_performance = 0
no_low_performance = 0

for p in power_readings:
    if p > 500:
        no_high_performance = no_high_performance + 1
    if p < 300:
        no_low_performance = no_low_performance + 1

print("=SOLAR PANEL DAILY READINGS=")
print(f"Total energy: {total_energy}W")
print(f"Average power output: {average_power_output}W")
print(f"Peak power: {max_power}W")
print(f"Lowest power: {lowest_power}W")
print(f"Number of high performance hours: {no_high_performance}")
print(f"Number of low performance hours: {no_low_performance}")

# SUBSTATION TRANSFORMER VOLTAGE MONITORING:
voltage_readings = [210, 245, 225, 265, 195, 220, 270, 240, 205, 215]
total_voltage = sum(voltage_readings)
counts = len(voltage_readings)
average_voltage = total_voltage/counts
Peak_voltage = max(voltage_readings)
lowest_voltage = min(voltage_readings)
voltage_range = Peak_voltage - lowest_voltage
safe_counts = 0
warning_counts = 0
critical_counts = 0
for v in voltage_readings:
    if v >= 200 and v <= 250:
        safe_counts = safe_counts + 1
    elif v >= 180 and v <= 200:
        warning_counts = warning_counts + 1
    else:
        critical_counts = critical_counts + 1

print(f"Average voltage: {average_voltage}V")
print(f"Peak voltage: {Peak_voltage}V")
print(f"Lowest voltage: {lowest_voltage}V")
print(f"Voltage range: {voltage_range}V")
print(f"Safe counts: {safe_counts}")
print(f"Warning counts: {warning_counts}")
print(f"Critical counts: {critical_counts}")