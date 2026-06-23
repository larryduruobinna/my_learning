voltage = 0
while voltage < 12:
    voltage = voltage + 2
    print(f"Charging... voltage is {voltage}")
print("BATTERY FULL!")

speed = 0
while speed < 3000:
    speed = speed + 500
    print(f"speed: {speed}rpm")
print("MOTOR AT MAX SPEED")

voltage = 0
while voltage < 48:
    voltage = voltage + 4
    if voltage == 32:
        print(f"Battery charging... {voltage}V - 50% charged")
    else:
        print(f"Battery charging... {voltage}V")
print("BANK FULLY CHARGED")


voltage = 11 
while voltage < 132:
    voltage = voltage + 11
    if voltage == 66:
        print(f"Transformer voltage level: {voltage}Kv - 50% STEPPED UP")
    else:
        print(f"Transformer voltage level: {voltage}Kv ")
print("TRANSMISSION VOLTAGE REACHED")

capacitor_charge = 0
while capacitor_charge < 100:
    capacitor_charge = capacitor_charge + 5
    if capacitor_charge == 50:
        print(f"Charge level: {capacitor_charge}V - HALF CHARGED")
    elif capacitor_charge == 75:
        print(f"Charge level: {capacitor_charge}V - 75% CHARGED")
    else:
        print(f"Charge level: {capacitor_charge}V")
print(f"CAPACITOR FULLY CHARGED")

power = 0
while power < 1500:
    power = power + 150
    print(f"Power increase: {power}Kw")
    if power == 750:
        print(f"Power increase: {power}Kw - 50% CAPACITY REACHED")
    elif power == 1200:
        print(f"Power increase: {power}Kw - WARNING! Near max power")
print("FULL POWER REACHED")