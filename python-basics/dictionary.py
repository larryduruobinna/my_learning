# DICTIONARY STORES DATA IN KEY - VALUE PAIRS.  LIKE A CONTROL PANEL WHERE EVERY SWITCH HAS A NAME AND A VALUE

panel = {"voltage": 230, "current": 15, "frequency": 50}
print(panel["voltage"])
print(panel["current"])
print(panel["frequency"])

panel["power"] = 3450  #Add new
panel["voltage"] = 240  #update existing
del panel["frequency"]  # delete
print(panel["voltage"])
print(panel["power"])
print(panel["current"])

#LOOP THROUGH
for key, value in panel.items():
    print(f"{key}:{value}")


# CHALLENGE

substation = {"voltage": 330, "current": 85, "frequency": 50, "status": "ONLINE"}
print(substation["voltage"])
print(substation["status"])

substation["power"] = substation["voltage"] * substation["current"]
del substation["frequency"]
if substation["power"] > 20000:
        substation["status"] = "OVERLOAD"
for key, value in substation.items():
    print(f"{key}: {value}")