# MOTOR POWER CONSUMPTION MONITOR:
power_consumptions = [45, 52, 48, 55, 50, 48, 53, 49]
total_power = sum(power_consumptions)
counts = len(power_consumptions)
average_consumption = total_power/counts
peak_power = max(power_consumptions)
Lowest_power = min(power_consumptions)
normal_hours = 0
warning_hours = 0
critical_hours = 0
for p in power_consumptions:
    if p >= 40 and p <= 50:
        normal_hours = normal_hours + 1
    elif p >= 50 and p <= 55:
        warning_hours =  warning_hours + 1
    else:
        critical_hours = critical_hours + 1

print(f"Average power: {average_consumption}KW")
print(f"Peak power: {peak_power}KW")
print(f"Lowest power: {Lowest_power}KW")
print(f"Total energy used: {total_power}KW")
print(f"Number of normal hours: {normal_hours}")
print(f"Number of warning hours: {warning_hours}")
print(f"Number of critical hours: {critical_hours}")
print("SAFE if no critical, DANGER if any critical")

# BUILDING ELECTRICAL SYSTEM HEALTH CHECK
voltage_readings = [218, 225, 230, 245, 220, 238, 242, 255,  235, 222]
total_voltage = sum(voltage_readings)
counts = len(voltage_readings)
average_voltage = total_voltage/counts
peak_voltage = max(voltage_readings)
lowest_voltage = min(voltage_readings)
voltage_stability = peak_voltage - lowest_voltage
safe_readings = 0
warning_readings = 0
critical_readings = 0
for v in voltage_readings:
    if v >= 220 and v < 240:
        safe_readings = safe_readings + 1
    elif v > 240 and v <= 250:
        warning_readings = warning_readings + 1
    else:
        critical_readings = critical_readings + 1
print(f"Average voltage: {average_voltage}V")
print(f"Peak voltage: {peak_voltage}V")
print(f"Lowest voltage: {lowest_voltage}V")
print(f"Voltage stability: {voltage_stability}V")
print(f"Counts for safe readings: {safe_readings}")
print(f"Counts for warning readings: {warning_readings}")
print(f"Counts for critical readings: {critical_readings}")
print(f"Overall status: HEALTHY-if no critical, ALERT-if critical exist")

# INDUSTRIAL POWER DISTRIBUTION NETWORK ANALYZER:

panel_1_loads = [120, 140, 130, 125, 135]
panel_2_loads = [200, 210, 190, 205, 200]
panel_3_loads = [80, 85, 90, 88, 92]
panel_4_loads = [150, 160, 155, 158, 152]
panel_5_loads = [250, 260, 255, 258, 252]
all_readings = panel_1_loads + panel_2_loads + panel_3_loads + panel_4_loads + panel_5_loads

total_load_1 = sum(panel_1_loads)
counts_1 = len(panel_1_loads)
average_load_1 = total_load_1/counts_1
peak_load_1 = max(panel_1_loads)
lowest_load_1 = max(panel_1_loads)
light_load_1 = average_load_1 < 150
medium_load_1 = 150 >= average_load_1 <= 300
heavy_load_1 = average_load_1 > 300

total_load_2 = sum(panel_2_loads)
counts_2 = len(panel_2_loads)
average_load_2 = total_load_2/counts_2
peak_load_2 = max(panel_2_loads)
lowest_load_2 = max(panel_2_loads)
light_load_2 = average_load_2 < 150
medium_load_2 = 150 >= average_load_2 <= 300
heavy_load_2 = average_load_2 > 300

total_load_3 = sum(panel_3_loads)
counts_3 = len(panel_3_loads)
average_load_3 = total_load_3/counts_3
peak_load_3 = max(panel_3_loads)
lowest_load_3 = max(panel_3_loads)
light_load_3 = average_load_3 < 150
medium_load_3 = 150 >= average_load_3 <= 300
heavy_load_3 = average_load_3 > 300

total_load_4 = sum(panel_4_loads)
counts_4 = len(panel_4_loads)
average_load_4 = total_load_4/counts_4
peak_load_4 = max(panel_4_loads)
lowest_load_4 = max(panel_4_loads)
light_load_4 = average_load_4 < 150
medium_load_4 = 150 >= average_load_4 <= 300
heavy_load_4 = average_load_4 > 300

total_load_5 = sum(panel_5_loads)
counts_5 = len(panel_5_loads)
average_load_5 = total_load_5/counts_5
peak_load_5 = max(panel_5_loads)
lowest_load_5 = min(panel_5_loads)
light_load_5 = average_load_5 < 150
medium_load_5 = 150 >= average_load_5 <= 300
heavy_load_5 = average_load_5 > 300

total_factory_load = [total_load_1, total_load_2, total_load_3, total_load_4, total_load_5]
sum_total_factoryload = sum(total_factory_load)
Highest_consuming_panel = max(total_factory_load)
lowest_consuming_panel = min(total_factory_load)
peak_load = max(all_readings)
if peak_load > 500:
    print("OVERLOAD!")
print(f"Peak load across ALL panels: {peak_load}")
print(f"Panel1: Total load: {total_load_1}KW| Average load: {average_load_1}KW| Peak load: {peak_load_1}KW| lowest_load: {lowest_load_1}KW|")
print(f"Panel2: Total load: {total_load_2}KW| Average load: {average_load_2}KW| Peak load: {peak_load_2}KW| lowest_load: {lowest_load_2}KW|")
print(f"Panel3: Total load: {total_load_3}KW| Average load: {average_load_3}KW| Peak load: {peak_load_3}KW| lowest_load: {lowest_load_3}KW|")
print(f"Panel4: Total load: {total_load_4}KW| Average load: {average_load_4}KW| Peak load: {peak_load_4}KW| lowest_load: {lowest_load_4}KW|")
print(f"Panel5: Total load: {total_load_5}KW| Average load: {average_load_5}KW| Peak load: {peak_load_5}KW| lowest_load: {lowest_load_5}KW|")
