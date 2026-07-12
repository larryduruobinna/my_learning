# BREAK: THINK OF IT LIKE CIRCUIT BREAKER THAT STRIPS WHEN A FAULT IS DETECTED. THE BREAK STOOPS A LOOP WHEN A IT SIGNAKS A FAULT.

current = 0 
while current < 100:
    current = current + 10
    if current == 60:
        print(f"Current: {current}A - OVERCURRENT!")
        break
    else:
        print(f"Current: {current}A")

voltage = 100 
while voltage < 1000:
    voltage = voltage + 100
    if voltage == 800:
        print(f"Voltage level: {voltage}V - HIGHVOLTAGE!")
        break
    else:
        print(f"Voltage level: {voltage}V")


# CONTINUE - THIS SKIPS ONE STEP AND CONTINUES GOING 
current = 0
while current < 24:
    current = current + 2
    if current == 12:
        print(f"Current level: {current}A - Average skipping")
        continue
    elif current == 18:
        print(f"Current level: {current}A - HIGH CURRENT!")
        break
    else:
        print(f"Current level: {current}A")


current = 0
while current < 100:
    current = current + 5
    if current == 35:
        print(f"Line current: {current}A - WARNING: NOISE DETECTED!")
        continue
    elif current == 75:
        print(f"Current level: {current}A - CRITICAL: LINE OVERLOADED!")
        break
    else:
        print(f"Current level: {current}A - OK!")



panels = [210, 240, 195, 260, 230, 180]
for p in panels:
    if p < 200:
        print(f"Voltage level: {p}V - SKIP!")
        continue
    elif p > 250:
        print(f"Voltage level: {p}V - STOP!")
        break
    else:
        print(f"Voltage level: {p}V - OK!")

temps = [45, 60, 75, 95, 55, 110]
for t in temps:
    if t < 50:
        print(f"Temps level: {t}C - SKIP!")
        continue
    elif t > 90:
        print(f"Temps level: {t}C - STOP!")
        break
    else:
        print(f"temps level: {t}C - OK!")

rpms = [800, 1200, 1500, 2200, 1800, 3000]
for r in rpms:
    if r < 1000:
        print(f"RPM: {r}RPM - SKIP!")
        continue
    elif r > 2000:
        print(f"RPM: {r}RPM - STOP!")
        break
    else:
        print(f"RPM: {r}RPM - OK!")