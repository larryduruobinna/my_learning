# ERROR HANDLING:
try:
    voltage = int(input("Enter voltage:"))
    print(f"VOLTAGE: {voltage}V")
except:
    print("ERROR: Please enter a number")


try:
    current = int(input("Enter current value:"))
    print(f"Current: {current}A")
except:
    print("Error Please enter a number")



# FINALLY: finally runs no matter what - error or no error.
try:
    voltage = int(input("Enter voltage value:"))
    print(f"Voltage: {voltage}V")
except:
    print("Error please enter a number")
finally:
    print("Complete Monitoring")


# CHALLENGE
try:
    current = int(input("Enter current value:"))
    voltage = 230
    power = current * voltage
    print(f"Power: {power}W")
except:
    print("Error please enter numbger!")