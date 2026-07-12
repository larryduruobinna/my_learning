# FUNCTION:
def greet_engineer():
    print("Welcome to the power plant!")
greet_engineer()



def check_voltage(voltage):
    print(f"Volatge: {voltage}V")

check_voltage(230)
check_voltage(415)

def check_power(power):
    print(f"Power is {power}W")
check_power(4500)
check_power(3000)
check_power(2000)


def check_voltage(voltage):
    if voltage < 200:
        print(f"VOLTAGE: {voltage}V - LOW!")
    elif voltage > 250:
        print(f"VOLTAGE: {voltage}V - HIGH!")
    else:
        print(f"VOLTAGE: {voltage}V - NORMAL!")
check_voltage(180)
check_voltage(230)
check_voltage(270)


def check_current(current):
    if current < 10:
        print(f"CURRENT: {current}A - LOW!")
    elif current > 25:
        print(f"CURRENT: {current}A - HIGH!")
    else:
        print(f"CURRENT: {current}A - NORMAL!")

check_current(30)
check_current(12)
check_current(2)



def calculate_power(voltage, current):
    power = voltage * current
    return power
result = calculate_power(230, 5)
print(f"POWER: {result}W")

def power(voltage, current):
    power = voltage * current
    return power

result = power(480, 25)
print(f"POWER: {result}W")



#CHALLENGE1
def check_current(current):
    if current < 10:
        print(f"Current: {current}A - SAFE!")
    elif current > 25:
        print(f"Current: {current}A - DANGER!")
    else:
        print(f"Current: {current}A - NORMAL!")
check_current(8)
check_current(20)
check_current(27)

# CHALLENGE2
def calculate_power(voltage, current):
    power = voltage * current
    return power
result = calculate_power(250, 5)
print(f"Power: {result}W")

# CHALLENGE3
def check_power(power):
    if power < 2000:
        print(f"Power: {power}W - LOW!")
    elif power > 4500:
        print(f"Power: {power}W - HIGH!")
    else:
        print(f"Power: {power}W - NORMAL!")
check_power(1800)
check_power(4600)
check_power(3500)
