#LOOPS IN DETAILS:
#TYPE 1: FOR LOOP WITH RANGE(), RANGE MAKES A LIST OF NUMBERS.
for i in range(5):
    print(i)
# range(5) means: numbers from 0 to 4. Python starts from 0.
# Range options:
range(5)      #0, 1, 2, 3, 4
range(1, 6)       # 1, 2, 3, 4, 5    starts from 1 and ends before 6
range(0, 10, 2)     # 0, 2, 4, 6, 8    starts from 0 ends before 10 and skips by 2
#For example:
#  CHECKING 10 MOTORS:
for motor_number in range(1, 11):
    print(f"Checking motor {motor_number}")
for temp_sensor in range(1, 30, 3):
    print(f"Check temperature sensor: {temp_sensor}")

# TYPE 2: FOR LOOP THROUGH A LIST
voltages = [220, 250, 260, 480, 600, 240, 208]
for v in voltages:
    print(f"Voltage readings: {v}V")
current = [15, 10, 12, 20, 25]
for c in current:
    print(f"Current readings: {c}A")
power = [4500, 3600, 6000, 7500]
for p in power:
    print(f"Power readings: {p}W")
    #the variable v becomes each item one at a time.


# TYPE 3: WHILE LOOP
#While loops keep going until something stops them.
voltage = 100
while voltage < 240:
    print(f"Voltage is now: {voltage} V")
    voltage = voltage + 20
print("Voltage reached 240!")

current = 10
while current > 2:
    print(f"Current is now: {current} A")
    current = current - 1
print("Current reached!")


power = 3000
while power < 4500:
    print(f"Power is now: {power}W")
    power = power + 100
print("Max power reached!")


#  LOOP WITH IF STATEMENT:
voltages = [210, 260, 220, 250, 208]
for v in voltages:
    if v > 240:
        print(f"{v} V - HIGH VOLTAGE!")
    else:
        print(f"{v} V - SAFE!")

currents = [5, 15, 8, 10, 7]
for c in currents:
    if c > 8:
        print(F"{c}A - HIGH CURRENT!")
    else:
        print(f"{c}A - NORMAL Safe")


# USEFUL LOOP TRICKS

