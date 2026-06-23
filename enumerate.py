# ENUMERATE: GIVES POSITIONING IN LISTS
readings = [120, 150, 200, 180, 190]
for position, value in enumerate(readings):
    print(f"Position {position}: Value {value}")
voltage = [450, 250, 480, 600, 460, 208]
for position, value in enumerate(voltage):
    print(f"Positiion {position}: Value {value}V")
current = [10, 2, 7, 15, 20]
for position, value in enumerate(current):
    print(f"Position {position}: Value {value}A")

powers = [200, 300, 400, 500, 600]
for position, power in enumerate(powers):
    if power > 400:
        print(f"Position {position} has {power} - CRITICAL!")

voltages = [400, 250, 300, 280, 220]
for position, voltage in enumerate(voltages):
    if voltage >= 300:
        print(f"position {position} has {voltage} - HIGH VOLTAGE!")



#CHALLENGE:
cell_voltages = [3.2, 2.8, 4.5, 3.1, 2.9, 4.1, 3.0, 3.3]
for position, cell_voltage in enumerate(cell_voltages):
    if cell_voltage < 3.0:
        print(f"cell{position} has {cell_voltage}V - BAD!")
    elif cell_voltage >= 3.0 and cell_voltage <= 4.2:
        print(f"cell{position} has {cell_voltage}V - NORMAL!")
    else:
        print(f"cell{position} has {cell_voltage}V - DANGER!")


# CHALLENGE2:
circuits = [15, 18, 22, 12, 25, 30, 14, 19]
total_circuits = len(circuits)
safe_count = 0
warning_count = 0
critical_count = 0
for position, circuit in enumerate(circuits):
    if circuit < 20:
        safe_count = safe_count + 1
        print(f"cicuit{position}: {circuit}A - SAFE!")
    elif circuit >= 20 and circuit <= 25:
        warning_count = warning_count + 1
        print(f"circuit{position}: {circuit}A - WARNING!")
    else:
        critical_count = critical_count + 1
        print(f"circuit{position}: {circuit}A - CRITICAL!")
print(f"total circuits: {total_circuits}")
print(f"safe count: {safe_count}")
print(f"warning count: {warning_count}")
print(f"critical count: {critical_count}")