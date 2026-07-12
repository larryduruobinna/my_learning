voltage = float(input("Enter voltage reading:"))
current = float(input("Enter current readings:"))
resistance = float(0.5)
power = voltage * current
power_loss = current*current*resistance
print(f"Power: {power}W")
print(f"Power loss: {power_loss}W")
if power < 10000:
    print(f"Power level: LIGHT LOAD")
elif power >= 10000 and power <= 50000:
    print(f"Power level: NORMAL LOAD")
else:
    print(f"Power level: HEAVY LOAD - Monitor closely")


# CHALLENGE 2:
currents = [45, 120, 78, 200, 55]
for c in currents:
    if c < 80:
        print(f"Cable reading: {c}A - SAFE!")
    elif c >= 80 and c <= 150:
        print(f"Cable reading: {c}A - CAUTION!")
    else:
        print(f"Cable reading: {c}A - DANGER!")
print("INSPECTION COMPLETE")

# CHALLENGE 3:
generators = [1200, 3500, 750, 4800, 2200]
max_safe_limit = float(input("What is your max safe limit?"))
safe_count = 0
print(max_safe_limit)
for g in generators:
    if g < max_safe_limit:
        print(f"Generator reading: {g}W - OK!")
        safe_count = safe_count + 1
    else:
        print(f"Generator reading: {g}W - OVERLOAD!")
print(f"Safe count: {safe_count}")


daily_output = [320, 415, 290, 510, 480, 195, 620]
total_output = sum(daily_output)
counts = len(daily_output)
average_output = round(total_output/counts, 2)
for position, d in enumerate(daily_output):
    position = position + 1
    if d < 300:
        print(f"Day {position}: {d}MW - LOW OUTPUT")
    elif d >= 300 and d <= 500:
        print(f"Day {position}: {d}MW - NORMAL OUTPUT")
    else:
        print(f"Day {position}: {d}MW - HIGH OUTPUT")
print(f"Total output: {total_output}MW")
print(f"Average output: {average_output}MW")

voltage = 180
while voltage < 240:
    voltage = voltage + 6
    if voltage == 210:
        print(f"Voltage level: {voltage}V - HALFWAY THERE")
    elif voltage == 228:
        print(f"Voltage level: {voltage}V - ALMOST THERE")
    else:
        print(f"Voltage level: {voltage}V")
print("VOLTAGE STABLE!")





