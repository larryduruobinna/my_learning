#IF STATEMENT
#CHALLENGE6
#BUILD A TRANSFORMER MONITORING SYSTEM
transformer_brand = input("Enter transformer name:")
primary_voltage = float(input("Enter primary voltage:"))
secondary_voltage = float(input("Enter seconary voltage:"))
load_current = float(input("Enter load current:"))
oil_temperature = float(input("Enter oil temp:"))
turns_ratio = primary_voltage/secondary_voltage
power = secondary_voltage*load_current

print("Transformer name:", transformer_brand)
print(f"Primary voltage: {primary_voltage}V")
print(f"Secondary voltage: {secondary_voltage}V")
print(f"Turns ratio: {turns_ratio}")
print(f"Load current: {load_current}A")
print(f"Power: {power}W")
print(f"Oil temperature: {oil_temperature}c")


if oil_temperature > 90:
    print("CRITICAL:Oil over heating - Shutdown required")
elif oil_temperature > 75:
    print("WARNING:High oil temperature")
elif oil_temperature > 60:
    print("CAUTION:Monitor temperature")
elif oil_temperature > 40:
    print("Normal operating temperature")
else:
    print("Cold start-waiting for normal operation")

if load_current < 50  and oil_temperature < 75:
    print("Status:HEALTHY")
elif load_current >= 50 and oil_temperature < 75:
    print("Status:HIGH LOAD")
elif oil_temperature >= 75:
    print("Status:DANGER")
else:
    print("Status:UNKNOWN - Check system")

