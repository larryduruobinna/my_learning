# GENERATOR LOAD MANAGEMENT SYSTEM
generator_name = input("What is the genrator name?")
capacity = float(input("what is the generator capacity?"))
voltage = float(input("What is the voltage rating?"))
current = float(input("What is the current load?"))
fuel_level = float(input("What is the fuel level?"))
operating_hours = float(input("What is the operating hours?"))
load_percentage = (current/capacity) * 100
available_capacity = capacity - current
estimated_hours_remaining = (fuel_level/100) * 12
print(f"Generator name:", generator_name)
print(f"Generator capacity: {capacity}KW")
print(f"Voltage rating: {voltage}V")
print(f"Current load: {current}KW")
print(f"Fuel level: {fuel_level}%")
print(f"Operating hours since last service: {operating_hours}")
print(load_percentage, "%")
print(available_capacity, "KW")
print(estimated_hours_remaining, "hrs")

# LOAD STATUS
if load_percentage > 90:
    print("CRITICAL-Reduce load immediately")
elif load_percentage > 80:
    print("WARNING-Approaching maximum")
elif load_percentage > 60:
    print("Moderate load")
elif load_percentage > 30:
    print("Normal operation")
else:
    print("Low load- inefficient")

# FUEL STATUS
if fuel_level < 10:
    print("EMPTY-Refuel now")
elif fuel_level < 25:
    print("LOW-Refuel soon")
elif fuel_level < 50:
    print("Half tank")
else:
    print("Adequate fuel")

# SERVICE STATUS
if operating_hours > 250:
    print("Service overdue")
elif operating_hours > 200:
    print("Service required")
elif operating_hours > 150:
    print("Service due soon")
else:
    print("Service not yet needed")


# USING LOGICAL OPERATORS
if fuel_level < 10 or load_percentage > 95:
    print("STOP GENERATOR IMMEDIATELY")
elif load_percentage > 80 and fuel_level < 25:
    print("EMERGENCY- High load with low fuel")
elif not load_percentage > 30:
    print("Generator is underused")
else:
    print("Normal operations")